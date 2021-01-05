from django.urls import re_path, include
from business.appelation.views import AppelationViewSet

urlpatterns = [
    re_path(r"", AppelationViewSet),
]
