from django.urls import re_path, include
from business.cepage.views import CepageViewSet

urlpatterns = [
    re_path(r"", CepageViewSet),
]
