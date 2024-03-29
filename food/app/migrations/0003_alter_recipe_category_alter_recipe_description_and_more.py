# Generated by Django 5.0.3 on 2024-03-25 17:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="category",
            field=models.CharField(
                choices=[("B", "Завтрак"), ("D", "Обед"), ("S", "Ужин")],
                max_length=1,
                verbose_name="Прием пищи",
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="description",
            field=models.TextField(verbose_name="Описание рецепта"),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="ingredients",
            field=models.ManyToManyField(
                to="app.ingredient", verbose_name="Ингредиенты"
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Название рецепта"),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="preview_image",
            field=models.CharField(max_length=255, verbose_name="Картинка"),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="time_minutes",
            field=models.IntegerField(
                default=1,
                help_text="В минутах",
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Время приготовления",
            ),
        ),
    ]
