from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from business.appellation.serializers import AppellationSerializer
from business.appellation.models import Appellation


class AppellationViewSet(ModelViewSet):
    queryset = Appellation.objects.all()
    serializer_class = AppellationSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.order_by("id")
