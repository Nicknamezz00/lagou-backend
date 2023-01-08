from django.contrib.auth import login
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_json_api.views import ModelViewSet
from rest_framework.mixins import CreateModelMixin

from coreutils.authentication import AnyAuthentication
from .models import UserProfile
from .serializers import (
    UserProfileSerializer,
    UserLoginSerializer,
    TokenSerializer,
    UserRegisterSerializer)


class UserProfileViewSet(ModelViewSet):

    permission_classes = [AllowAny, ]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    # TODO: `create` permission.
    # def create(self, request, *args, **kwargs):


class UserLoginAPIView(GenericAPIView, CreateModelMixin):

    resource_name = 'login'
    permission_classes = [AllowAny, ]
    authentication_classes = [AnyAuthentication, ]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            token, _ = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response(
                data=TokenSerializer(token).data,
                status=status.HTTP_200_OK)
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


class UserRegisterAPIView(CreateAPIView):

    resource_name = 'register'
    permission_classes = [AllowAny, ]
    authentication_classes = [AnyAuthentication, ]
    serializer_class = UserRegisterSerializer
