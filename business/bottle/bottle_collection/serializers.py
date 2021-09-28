from rest_framework import serializers
from business.grape.serializers import GrapeSerializer
from business.bottle.bottle_collection.models import BottleCollection


class BottleCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottleCollection
        fields = "__all__"

    def to_representation(self, instance):
        serializer_data = super().to_representation(instance)
        serializer_data["grape"] = GrapeSerializer(
            instance.grape.all(), many=True
        ).data
        serializer_data["appellation"] = instance.appellation.name
        return serializer_data