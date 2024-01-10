from django import forms
from ckeditor.fields import CKEditorWidget

from .models import Recipe


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ["name", "preview_image", "time_minutes", "category", "ingredients", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "preview_image": forms.FileInput(attrs={"class": "form-control"}),
            "time_minutes": forms.NumberInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "ingredients": forms.SelectMultiple(attrs={"class": "form-control"}),
            "description": CKEditorWidget()
        }
