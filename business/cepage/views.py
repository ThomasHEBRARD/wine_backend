from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from business.cepage.serializers import CepageSerializer
from business.cepage.models import Cepage


class CepageViewSet(ModelViewSet):
    queryset = Cepage.objects.all()
    serializer_class = CepageSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.order_by("id")
