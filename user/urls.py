from django.urls import include, path
from rest_framework import routers
from user.user.views import UserRegistrationViewSet

router = routers.DefaultRouter()
router.register(r"register", UserRegistrationViewSet)

urlpatterns = [path("", include(router.urls))]
