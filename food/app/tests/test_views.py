from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from app.models import Recipe, Ingredient
from .extra import get_fake_image

User = get_user_model()


class TestCreateRecipeView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ingredient = Ingredient.objects.create(name="test")
        cls.user = User.objects.create_user(
            username='TestCreateRecipeView_user',
            email="TestCreateRecipeView@mail",
            password="TestCreateRecipeView_password",
        )

    def test_create_recipe(self):
        self.client.force_login(self.user)
        self.assertEqual(
            0,
            Recipe.objects.all().count(),
        )

        res = self.client.post(reverse("create-recipe"), {
            "name": "тестовый рецепт",
            "preview_image": get_fake_image(),
            "time_minutes": 12,
            "category": "B",
            "ingredients": [self.ingredient.id],
            "description": "desc",
        })

        self.assertEqual(302, res.status_code)  # После успешного создания перенаправляет

        self.assertEqual(
            1,
            Recipe.objects.all().count(),
        )

        recipe = Recipe.objects.get(user=self.user)

        self.assertEqual("тестовый рецепт", recipe.name)
        self.assertEqual("desc", recipe.description)

    def test_create_recipe_without_user(self):
        res = self.client.get(reverse("create-recipe"))
        self.assertRedirects(res, reverse("login") + "?next=" + reverse("create-recipe"))

        res = self.client.post(reverse("create-recipe"))
        self.assertRedirects(res, reverse("login") + "?next=" + reverse("create-recipe"))


class TestUpdateRecipeView(TestCase):
    ingredient = None
    owner_user = None
    recipe = None

    @classmethod
    def setUpTestData(cls):
        cls.ingredient = Ingredient.objects.create(name="name")
        cls.owner_user = User.objects.create_user(
            username='TestUpdateRecipeView_owner_user',
            email="TestUpdateRecipeView_owner_user@mail",
            password="TestUpdateRecipeView_password",
        )
        cls.other_user = User.objects.create_user(
            username='TestUpdateRecipeView_other_user',
            email="TestUpdateRecipeView_other_user@mail",
            password="TestUpdateRecipeView_password",
        )
        cls.recipe = Recipe.objects.create(
            name="тестовый рецепт",
            preview_image="image",
            time_minutes=12,
            user=cls.owner_user,
            category="B",
            description="desc",
        )
        cls.recipe.ingredients.add(cls.ingredient)

        cls.url = reverse("update-recipe", args=[cls.recipe.id])

    def test_owner_user_update(self):
        self.client.force_login(self.owner_user)
        res = self.client.post(self.url, {
            "name": "НАЗВАНИЕ РЕЦЕПТА",
            "preview_image": get_fake_image(),
            "time_minutes": 12,
            "category": "B",
            "ingredients": [self.ingredient.id],
            "description": "desc",
        })
        self.assertRedirects(res, reverse("show-recipe", args=(self.recipe.id,)))

        self.assertEqual(1, Recipe.objects.filter(name="НАЗВАНИЕ РЕЦЕПТА").count())

    def test_other_user_update(self):
        self.client.force_login(self.other_user)

        res = self.client.post(self.url, {
            "name": "НАЗВАНИЕ РЕЦЕПТА",
            "preview_image": get_fake_image(),
            "time_minutes": 12,
            "category": "B",
            "ingredients": [self.ingredient.id],
            "description": "desc",
        })

        self.assertEqual(403, res.status_code)

        self.assertEqual(0, Recipe.objects.filter(name="НАЗВАНИЕ РЕЦЕПТА").count())
