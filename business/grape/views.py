from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from business.grape.serializers import GrapeSerializer
from business.grape.models import Grape


class GrapeViewSet(ModelViewSet):
    queryset = Grape.objects.all()
    serializer_class = GrapeSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.order_by("id")
