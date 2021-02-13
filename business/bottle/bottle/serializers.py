from rest_framework import serializers
from business.bottle.bottle.models import Bottle


class BottleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bottle
        fields = "__all__"
