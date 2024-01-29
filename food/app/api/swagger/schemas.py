from drf_yasg.utils import swagger_auto_schema

from ..serializers import RecipeSerializer


recipes_api_doc = swagger_auto_schema(
    responses={
        201: RecipeSerializer(),
        400: "Bad Request",
        401: "Unauthorized",
        500: "Internal Server Error",
    }
)
