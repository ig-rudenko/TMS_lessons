from rest_framework import serializers

from app.models import Recipe


class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["id", "name", "preview_image", "created_at", "time_minutes", "user", "ingredients", "category"]


class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["name", "preview_image", "description", "created_at", "time_minutes", "ingredients", "category"]


class RecipeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["id", "name", "preview_image", "description", "created_at", "time_minutes", "ingredients", "category",
                  "user"]
