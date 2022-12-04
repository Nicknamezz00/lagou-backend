from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)

from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(
        ListModelMixin,
        RetrieveModelMixin,
        UpdateModelMixin,
        viewsets.GenericViewSet
        ):

    permission_classes = [AllowAny, ]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
