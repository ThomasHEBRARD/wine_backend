from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path("admin/", admin.site.urls),
    re_path(r"^", include("business.urls")),
    re_path(r"^", include("user.urls")),
]
