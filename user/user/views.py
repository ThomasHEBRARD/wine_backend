from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user.user.serializers import UserRegistrationSerializer, UserLoginSerializer
from user.user.models import User

class UserRegistrationViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            "success": "True",
            "status_code": status_code,
            "message": "User registered successfully",
        }
        return Response(response, status_code=status_code)


class UserLoginViewSet(RetrieveAPIView, ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        status_code = status.HTTP_200_OK
        response = {
            "success": "True",
            "status_code": status_code,
            "message": "User logged in successfully",
            "token": serializer.data["token"],
        }

        return Response(response, status=status_code)
