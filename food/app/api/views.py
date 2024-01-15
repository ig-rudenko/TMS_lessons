from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer

from app.models import Recipe
from .serializers import RecipeListSerializer, RecipeCreateSerializer, RecipeDetailSerializer


class ListCreateAPIView(GenericAPIView):
    """
    Класс API view, для endpoint'a просмотра перечня рецептов и создания новых.
    """
    queryset = Recipe.objects.all()  # Как и где достать наши объекты

    def get_serializer_class(self):
        """В зависимости от метода HTTP возвращает соответствующий класс для создания сериализатора"""
        if self.request.method == 'POST':
            return RecipeCreateSerializer
        return RecipeListSerializer

    def get(self, request, *args, **kwargs):
        """
        Метод `get` вызывается автоматический, когда HTTP метод запроса является `GET`.
        """
        queryset = self.get_queryset()
        serializer: ModelSerializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Метод `post` вызывается автоматический, когда HTTP метод запроса является `POST`.
        """
        serializer: ModelSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        recipe = serializer.save(user=self.request.user)

        serializer = RecipeDetailSerializer(instance=recipe)
        return Response(serializer.data, status=201)


@api_view()  # Это только для функций
def list_create_recipe_api_view(request):
    res = []
    for recipe in Recipe.objects.all():
        object_dict = {
            "id": recipe.id,
            "name": recipe.name,
            "preview_image": recipe.preview_image.url,
            "created_at": recipe.created_at,
            "time_minutes": recipe.time_minutes,
            "user": recipe.user.id,
            "ingredients": recipe.ingredients.all().values_list("name", flat=True),
            "category": recipe.category
        }
        res.append(object_dict)

    return Response(res)


@api_view()  # Это только для функций
def detail_recipe_api_view(request, pk: int):
    recipe = get_object_or_404(Recipe, id=pk)
    object_dict = {
        "id": recipe.id,
        "name": recipe.name,
        "description": recipe.description,
        "preview_image": recipe.preview_image.url,
        "created_at": recipe.created_at,
        "time_minutes": recipe.time_minutes,
        "user": recipe.user.id,
        "ingredients": recipe.ingredients.all().values_list("name", flat=True),
        "category": recipe.category
    }
    return Response(object_dict)
