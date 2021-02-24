from django.urls import include, path
from rest_framework import routers
from business.bottle.bottle_collection.views import BottleCollectionViewSet
from business.bottle.bottle.views import BottleViewSet
from business.cellar.views import CellarViewSet
from business.cepage.views import CepageViewSet
from business.appelation.views import AppelationViewSet

router = routers.DefaultRouter()
router.register(r"bottles", BottleViewSet)
router.register(r"bottle_collection", BottleCollectionViewSet)
router.register(r"cellar", CellarViewSet)
router.register(r"cepages", CepageViewSet)
router.register(r"appelations", AppelationViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
