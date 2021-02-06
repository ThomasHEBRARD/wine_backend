from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .serializers import BottleSerializer
from business.bottle.bottle.models import Bottle
from rest_framework.response import Response
from rest_framework.decorators import action


class BottleViewSet(ModelViewSet):
    queryset = Bottle.objects.all()
    serializer_class = BottleSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.order_by("id")

    @action(methods=["get"], detail=False)
    def get_bottles(self, request):
        serializer = self.get_serializer(
            Bottle.objects.filter(name__icontains=request.data.get("name")), many=True
        )
        return Response(serializer.data)
