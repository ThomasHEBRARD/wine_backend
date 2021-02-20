from rest_framework import serializers
from business.bottle.bottle_collection.models import BottleCollection


class BottleCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottleCollection
        fields = "__all__"
