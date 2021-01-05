from rest_framework import serializers
from business.appelation.models import Appelation


class AppelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appelation
        fields = "__all__"
