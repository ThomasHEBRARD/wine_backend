from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from business.bottle.serializers import BottleSerializer
from business.bottle.models import Bottle


class BottleViewSet(ModelViewSet):
    queryset = Bottle.objects.all()
    serializer_class = BottleSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.order_by("id")
