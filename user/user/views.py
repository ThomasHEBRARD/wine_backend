from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user.user.serializers import UserRegistrationSerializer
from user.user.models import User

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    pass

class UserRegistrationViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            "success": "True",
            "status_code": status_code,
            "message": "User registered successfully"
        }
        return Response(response, status_code=status_code)