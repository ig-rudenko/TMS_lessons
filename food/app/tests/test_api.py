import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from app.models import Ingredient

User = get_user_model()


class TestRecipeListCreateAPIView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.ingredient = Ingredient.objects.create(name="test")
        cls.user = User.objects.create_user(
            username='TestCreateRecipeView_user',
            email="TestCreateRecipeView@mail",
            password="TestCreateRecipeView_password",
        )
        cls.url = reverse("recipes_api:recipes-list-create")

    def test_create_recipe(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            self.url,
            json.dumps({
                "name": "тестовый рецепт",
                "preview_image": "/images/test.png",
                "time_minutes": 12,
                "category": "B",
                "ingredients": [
                    {
                        "name": self.ingredient.name
                    }
                ],
                "description": "desc",
            }),
            content_type="application/json"
        )
        print(response.data)
        self.assertEqual(201, response.status_code)

    def test_create_recipe_without_user(self):
        response = self.client.post(self.url)
        self.assertEqual(401, response.status_code)

    def test_create_recipe_invalid_category(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            self.url,
            json.dumps({
                "name": "тестовый рецепт",
                "preview_image": "/images/test.png",
                "time_minutes": 12,
                "category": "test_create_recipe_invalid_category",
                "ingredients": [
                    {
                        "name": self.ingredient.name
                    }
                ],
                "description": "desc",
            }),
            content_type="application/json"
        )
        print(response.data)
        self.assertEqual(400, response.status_code)
        self.assertIn("category", response.data)

    def test_create_recipe_with_new_ingredient(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            self.url,
            json.dumps({
                "name": "тестовый рецепт",
                "preview_image": "/images/test.png",
                "time_minutes": 12,
                "category": "test_create_recipe_invalid_category",
                "ingredients": [
                    {
                        "name": "new",
                    }
                ],
                "description": "desc",
            }),
            content_type="application/json"
        )
        print(response.data)
        self.assertEqual(201, response.status_code)

    def test_create_recipe_invalid_time_minutes(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            self.url,
            json.dumps({
                "name": "тестовый рецепт",
                "preview_image": "/images/test.png",
                "time_minutes": -100,
                "category": "test_create_recipe_invalid_category",
                "ingredients": [
                    {
                        "name": "new",
                    }
                ],
                "description": "desc",
            }),
            content_type="application/json"
        )
        print(response.data)
        self.assertEqual(400, response.status_code)
        self.assertIn("time_minutes", response.data)
