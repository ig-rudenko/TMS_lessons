from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from .swagger.schemas import token_obtain_pair_api_doc


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @token_obtain_pair_api_doc
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
