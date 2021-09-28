from django.urls import re_path, include
from business.appellation.views import AppellationViewSet

urlpatterns = [
    re_path(r"", AppellationViewSet),
]
