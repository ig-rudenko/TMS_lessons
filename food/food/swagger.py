from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from users.api.views import DecoratedTokenObtainPairView


schema_view = get_schema_view(
    openapi.Info(
        title="Recipes API",
        default_version='v 1.0.1',
        description="API для создания и просмотра рецептов",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(name="igor", email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[JWTAuthentication],
    patterns=[
        path("api/recipes/", include("app.api.urls")),
        # JWT
        path('api/token/', DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ]
)
