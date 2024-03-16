from django.urls import path

from . import views

# /recipe/

urlpatterns = [
    path('create/', views.create_recipe, name='create-recipe'),
    path('update/<int:recipe_id>', views.update_recipe, name='update-recipe'),
    path('delete/<int:recipe_id>', views.delete_recipe, name='delete-recipe'),
    path('<int:recipe_id>', views.show_recipe, name='show-recipe'),
    path("favorites", views.ListFavoriteRecipesView.as_view(), name='show-favorite-recipes'),
    path("favorite/<int:recipe_id>", views.MakeFavoriteView.as_view(), name='make-favorite-recipe')
]
