from rest_framework import serializers
from business.cellar.models import Cellar


class CellarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cellar
        fields = "__all__"
