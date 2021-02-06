from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("business.urls")),
    path("api/", include("user.urls"))
    ]
