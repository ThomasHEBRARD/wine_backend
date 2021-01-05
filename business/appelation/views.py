from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from business.appelation.serializers import AppelationSerializer
from business.appelation.models import Appelation


class AppelationViewSet(ModelViewSet):
    queryset = Appelation.objects.all()
    serializer_class = AppelationSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.order_by("id")
