from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .serializers import BottleCollectionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from business.bottle.bottle_collection.models import BottleCollection
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK


class BottleCollectionViewSet(ModelViewSet):
    queryset = BottleCollection.objects.all()
    serializer_class = BottleCollectionSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["name"]
    search_fields = ["name"]

    def get_queryset(self):
        return self.queryset.order_by("id")

    @action(methods=["GET"], detail=False)
    def add_bottle(self, request):
        return Response(serializer.data, status=HTTP_200_OK)
