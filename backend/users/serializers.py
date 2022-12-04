from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import UserProfile


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        exclude = ['preferred_language']
