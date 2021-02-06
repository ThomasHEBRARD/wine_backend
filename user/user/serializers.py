from rest_framework import serializers
from user.user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "password", "email")
        extra_kwargs = {"password": {"write_only" : True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user