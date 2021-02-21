from django.conf.urls import url
from django.urls import re_path, include, path
from rest_framework.routers import SimpleRouter
from user.user.views import UserRegistrationViewSet, UserLoginViewSet, UserLogoutViewSet, UserViewSet


router = SimpleRouter()
router.register("login", UserLoginViewSet)
router.register("register", UserRegistrationViewSet)
router.register("user", UserViewSet)

urlpatterns = [
     re_path(r"^", include(router.urls)), 
     path("logout/", UserLogoutViewSet.as_view())
     ]
