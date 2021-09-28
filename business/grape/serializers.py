from rest_framework import serializers
from business.grape.models import Grape


class GrapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grape
        fields = ["name", "proportion"]
