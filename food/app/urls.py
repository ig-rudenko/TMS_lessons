from django.urls import path

from .views import create_recipe, home

# /recipe/

urlpatterns = [
    path('create/', create_recipe, name='create-recipe')
]
