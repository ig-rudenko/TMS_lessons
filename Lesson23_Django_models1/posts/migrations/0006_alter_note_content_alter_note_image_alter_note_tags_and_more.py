# Generated by Django 5.0 on 2024-02-12 18:18

import django.db.models.deletion
import django_ckeditor_5.fields
import posts.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_tag_note_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Содержимое'),
        ),
        migrations.AlterField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to, verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(related_name='notes', to='posts.tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(help_text='Укажите не более 255 символов', max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
    ]