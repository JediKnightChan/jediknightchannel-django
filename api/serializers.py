from rest_framework import serializers
from .models import LoginRequest


class LoginRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginRequest
        fields = ('id', 'ip', 'social_network', 'stage')
