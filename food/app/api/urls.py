from django.urls import path

from . import views

# /api/

app_name = 'api'

urlpatterns = [
    # Классы представлений указываем через вызов метода `as_view`
    path("recipes/", views.ListCreateAPIView.as_view(), name="recipes-list-create"),
    path("recipes/<int:pk>", views.detail_recipe_api_view, name="recipe"),
]
