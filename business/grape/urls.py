from django.urls import re_path, include
from business.grape.views import GrapeViewSet

urlpatterns = [
    re_path(r"", GrapeViewSet),
]
