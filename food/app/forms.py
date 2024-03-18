from django import forms
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from ckeditor.fields import CKEditorWidget

from .models import Recipe


class RecipeForm(forms.ModelForm):
    preview_image = forms.ImageField(required=True)
    description = forms.CharField(
        widget=CKEditorWidget(),
        required=True,
        label=""
    )

    class Meta:
        model = Recipe
        fields = ["name", "preview_image", "time_minutes", "category", "ingredients", "description"]

    def save(self, commit=True):
        image: InMemoryUploadedFile = self.cleaned_data["preview_image"]

        self.instance.preview_image = f"images/{image.name}"

        with default_storage.open(self.instance.preview_image, "wb") as image_file:
            image_file.write(image.read())
        return super().save(commit)
