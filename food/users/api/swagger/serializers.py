from rest_framework import serializers


class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField(label='Access Token')
    refresh = serializers.CharField(label='Refresh Token')
