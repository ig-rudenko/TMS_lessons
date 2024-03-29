from django.urls import path

from . import views

# /api/recipes/

app_name = 'recipes_api'

urlpatterns = [
    # Классы представлений указываем через вызов метода `as_view`
    path("", views.RecipeListCreateAPIView.as_view(), name="recipes-list-create"),
    path("<int:pk>", views.RecipeDetailAPIView.as_view(), name="recipe"),
    path("image", views.UploadImageAPIView.as_view(), name="recipe-image-upload"),
]
