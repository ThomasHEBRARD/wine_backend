from django.conf.urls import url
from django.urls import re_path
from user.user.views import UserRegistrationViewSet

urlpatterns = [
     re_path(r"", UserRegistrationViewSet),
]