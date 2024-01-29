from drf_yasg.utils import swagger_auto_schema

from .serializers import TokenObtainPairResponseSerializer


token_obtain_pair_api_doc = swagger_auto_schema(
    responses={
        200: TokenObtainPairResponseSerializer(),
        400: "Bad Request",
        500: "Internal Server Error",
    }
)
