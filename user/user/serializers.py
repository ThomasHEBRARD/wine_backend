from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from user.user.models import User
from business.cellar.models import Cellar


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class UserRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    token = serializers.CharField(max_length=255, read_only=True)

    def create(self, data):
        user = User.objects.create_user(**data)
        Cellar.objects.create(name="My Cellar", code=user.email, user=user)

        try:
            payload = api_settings.JWT_PAYLOAD_HANDLER(user)
            jwt_token = api_settings.JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "User with given email and password does not exists"
            )
        return {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "token": jwt_token,
        }


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def create(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                "A user with this email and password is not found"
            )

        try:
            payload = api_settings.JWT_PAYLOAD_HANDLER(user)
            jwt_token = api_settings.JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "User with given email and password does not exists"
            )
        return {"email": user.email, "token": jwt_token}
