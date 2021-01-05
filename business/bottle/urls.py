from django.urls import re_path, include
from business.bottle.views import BottleViewSet

urlpatterns = [
    re_path(r"", BottleViewSet),
]
