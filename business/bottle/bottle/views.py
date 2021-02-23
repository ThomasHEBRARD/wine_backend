from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .serializers import BottleSerializer
from business.bottle.bottle.models import Bottle
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK
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

    # form of answer: [{'bottleId': xxxx, 'stockToRemove': xxx}, .. ]
    @action(methods=["POST"], detail=False)
    def remove_bottles(self, request):
        list_of_bottles_to_remove = request.data
        user = request.user
        for bottle_info_to_remove in list_of_bottles_to_remove: 
            bottle_to_update = Bottle.objects.get(cellar__user=user, bottle_collection__id=bottle_info_to_remove["bottleId"])
            bottle_to_update.stock -= bottle_info_to_remove["stockToRemove"]
            bottle_to_update.save()
            if bottle_to_update.stock == 0:
                bottle_to_update.delete()
        return Response(status=HTTP_200_OK)