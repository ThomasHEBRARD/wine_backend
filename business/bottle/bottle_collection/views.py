from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .serializers import BottleCollectionSerializer
from business.bottle.bottle_collection.models import BottleCollection
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


class BottleCollectionViewSet(ModelViewSet):
    queryset = BottleCollection.objects.all()
    serializer_class = BottleCollectionSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.order_by("id")
