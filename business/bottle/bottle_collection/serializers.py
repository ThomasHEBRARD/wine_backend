from rest_framework import serializers
from business.cepage.serializers import CepageSerializer
from business.bottle.bottle_collection.models import BottleCollection


class BottleCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottleCollection
        fields = "__all__"

    def to_representation(self, instance):
        serializer_data = super().to_representation(instance)
        serializer_data["cepage"] = CepageSerializer(
            instance.cepage.all(), many=True
        ).data
        serializer_data["appellation"] = instance.appellation.name
        return serializer_data