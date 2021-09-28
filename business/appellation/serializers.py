from rest_framework import serializers
from business.appellation.models import Appellation


class AppellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appellation
        fields = "__all__"
