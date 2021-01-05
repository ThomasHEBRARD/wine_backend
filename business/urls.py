from django.urls import include, path
from rest_framework import routers
from business.bottle.views import BottleViewSet
from business.cellar.views import CellarViewSet

router = routers.DefaultRouter()
router.register(r'bottles', BottleViewSet)
router.register(r'cellar', CellarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]