"""
URL configuration for Lesson21_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

from posts.views import home_page_view, create_note_view, show_note_view, filter_notes_view

urlpatterns = [
    path('admin/', admin.site.urls),  # Подключение панели администратора.
    path('accounts/', include("django.contrib.auth.urls")),
    # path('login', LoginView.as_view()),

    path("", home_page_view, name="home"),  # Добавим главную страницу.
    path("filter", filter_notes_view, name="filter-notes"),
    path("create", create_note_view, name="create-note"),
    path("post/<note_uuid>", show_note_view, name="show-note"),
]
