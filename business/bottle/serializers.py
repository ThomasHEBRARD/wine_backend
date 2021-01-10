from rest_framework import serializers
from business.bottle.models import Bottle


class BottleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bottle
        fields = ["name"]
