from rest_framework import serializers
from business.bottle.bottle.models import Bottle


class BottleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bottle
        fields = ["stock"]

    def to_representation(self, instance):
        serializer_data = super().to_representation(instance)
        serializer_data["name"] = instance.bottle_collection.name
        return serializer_data