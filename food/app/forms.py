from django import forms
from ckeditor.fields import CKEditorWidget

from .models import Recipe


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ["name", "preview_image", "time_minutes", "category", "ingredients", "description"]
        widgets = {
            "description": CKEditorWidget()
        }
