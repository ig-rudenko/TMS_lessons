from typing import cast

from celery.canvas import chain
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.core.cache import cache
from django.db.models import Case, When, Value, Subquery, OuterRef, Func
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from users.models import User
from .cache import get_or_cache
from .favorite_service import FavoriteRecipesService
from .forms import RecipeForm
from .models import Recipe, Ingredient
from .tasks import check_recipe_content, send_email_task


class GroupConcat(Func):
    function = 'STRING_AGG'
    template = '%(function)s(%(expressions)s)'


def home(request: WSGIRequest):
    recipes_queryset = (
        Recipe.objects.annotate(
            ingredients_list=Subquery(
                Ingredient.objects
                .filter(recipe=OuterRef('pk'))
                .values('recipe')
                .annotate(
                    names=GroupConcat('name', Value(" "), distinct=True)
                )
                .values('names')[:1]
            )
        )
        .values("id", "name", "time_minutes", "preview_image", "ingredients_list", "category")
    )

    search = request.GET.get("search")
    if search:
        recipes_data = recipes_queryset.filter(description__search=search)
    else:
        recipes_data = get_or_cache("home-page-recipes", recipes_queryset)  # type: ignore

    return render(request, 'home.html', {"recipes": recipes_data})


@login_required
def create_recipe(request: WSGIRequest):
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)  # Файлы находятся отдельно!
        if form.is_valid():
            recipe: Recipe = form.save(commit=False)  # Не сохранять в базу рецепт, а вернуть его объект.
            recipe.user = cast(User, request.user)
            recipe.save()  # Сохраняем в базу объект.
            form.save_m2m()  # Сохраняем отношения many to many для ингредиентов и рецепта.

            # Задача на проверку орфографии.
            chain(
                check_recipe_content.s(recipe.id),
                send_email_task.s(recipe.user.email, "Рецепт был проверен на ошибки")
            )()
            cache.delete("home-page-recipes")

            return HttpResponseRedirect("/")

    return render(request, 'recipe/create-form.html', {'form': form})


@login_required
def update_recipe(request: WSGIRequest, recipe_id: int):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.user != request.user:
        return HttpResponseForbidden("You do not have permission to edit this recipe")

    form = RecipeForm(instance=recipe)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)  # Файлы находятся отдельно!
        if form.is_valid():
            recipe = form.save()
            return HttpResponseRedirect(reverse("show-recipe", args=(recipe.id,)))

    return render(request, 'recipe/update-form.html', {'form': form, "recipe": recipe})


@login_required
def delete_recipe(request: WSGIRequest, recipe_id: int):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.user != request.user:
        return HttpResponseForbidden("You do not have permission to delete this recipe")
    recipe.delete()
    cache.delete("home-page-recipes")
    return HttpResponseRedirect(reverse("home"))


def show_recipe(request: WSGIRequest, recipe_id: int):
    recipe: Recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, "recipe/recipe.html", {"recipe": recipe})


class ListFavoriteRecipesView(View):
    def get(self, request: WSGIRequest):
        """
        Метод `get` вызывается автоматический, когда HTTP метод запроса является `GET`.
        """
        favorite_service = FavoriteRecipesService(request)
        ids = favorite_service.favorites_ids[::-1]
        ordering = Case(*[When(id=ident, then=pos) for pos, ident in enumerate(ids)])
        queryset = Recipe.objects.filter(id__in=ids).order_by(ordering)

        search = request.GET.get("search")
        if search:
            queryset = queryset.filter(description__search=search)
        return render(request, "recipe/favorite.html", {"recipes": queryset})


class MakeFavoriteView(View):
    def post(self, request: WSGIRequest, recipe_id: int):
        """
        Метод `post` вызывается автоматический, когда HTTP метод запроса является `POST`.
        """
        recipe: Recipe = get_object_or_404(Recipe, id=recipe_id)
        self.make_favorite(request, recipe)
        return HttpResponseRedirect(reverse("show-recipe", args=(recipe.id,)))

    @staticmethod
    def make_favorite(request: WSGIRequest, recipe: Recipe):
        favorite_service = FavoriteRecipesService(request)
        if request.POST.get('favorite') == "no":
            favorite_service.remove_favorite(recipe.id)
        else:
            favorite_service.add_favorite(recipe)
