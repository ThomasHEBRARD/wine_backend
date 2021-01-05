from rest_framework import serializers
from business.cepage.models import Cepage


class CepageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cepage
        fields = "__all__"
