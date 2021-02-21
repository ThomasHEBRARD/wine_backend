from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from business.cellar.serializers import CellarSerializer
from business.cellar.models import Cellar


class CellarViewSet(ModelViewSet):
    queryset = Cellar.objects.all()
    serializer_class = CellarSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset
