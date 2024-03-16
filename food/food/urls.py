"""
URL configuration for food project.

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
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from app.views import home
from users.api.views import DecoratedTokenObtainPairView
from .swagger import schema_view

# /

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path("api/recipes/", include("app.api.urls")),
    # Token
    path("api/auth/", include("djoser.urls.authtoken")),
    # JWT
    path('api/token/', DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Other
    path("account/", include("users.urls")),  # связь с приложением users.
    path("recipe/", include("app.urls")),  # связь с приложением app.
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    # DOCS
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Prometheus
    path('', include('django_prometheus.urls')),
]
