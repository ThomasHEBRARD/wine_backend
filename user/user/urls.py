from django.conf.urls import url
from django.urls import re_path, include
from rest_framework.routers import SimpleRouter
from user.user.views import UserRegistrationViewSet, UserLoginViewSet


router = SimpleRouter()
router.register("login", UserLoginViewSet)
router.register("register", UserRegistrationViewSet)

urlpatterns = [
     re_path(r"^", include(router.urls)), 
     ]
