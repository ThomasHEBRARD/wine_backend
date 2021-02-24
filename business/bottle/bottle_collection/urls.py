from django.urls import re_path, include
from business.bottle.bottle_collection.views import BottleCollectionViewSet

urlpatterns = [
    re_path(r"", BottleCollectionViewSet),
]
