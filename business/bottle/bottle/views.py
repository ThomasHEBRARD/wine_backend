from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .serializers import BottleSerializer
from business.bottle.bottle.models import Bottle
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


class BottleViewSet(ModelViewSet):
    queryset = Bottle.objects.all()
    serializer_class = BottleSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter]
    search_fields = ["bottle_collection__name"]

    # test with 5 millions bottles
    # look into his bottles
    # filter by user before filtering
    def get_queryset(self):
        return self.queryset.filter(
            cellar__user__email=self.request.user.email
        ).prefetch_related("bottle_collection")
