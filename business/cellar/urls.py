from django.urls import re_path, include
from business.cellar.views import CellarViewSet

urlpatterns = [
    re_path(r"", CellarViewSet),
]
