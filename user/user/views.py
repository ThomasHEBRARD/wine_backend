from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from user.user.serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer
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

class UserLogoutViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    @classmethod
    def post(cls, request):
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer