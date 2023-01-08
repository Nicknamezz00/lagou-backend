from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from rest_framework_json_api import serializers

from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['groups', 'user_permissions', 'password']


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False)

    class Meta:
        model = UserProfile
        exclude = ['id', 'preferred_language']
        # fields = ['user']


class UserLoginSerializer(serializers.Serializer):

    class Meta:
        resource_name = "login"

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    default_error_messages = {
        'inactive_account': _('User account is disabled.'),
        'invalid_credentials': _('Unable to login with provided credentials.')
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(
            username=attrs.get('username'),
            password=attrs.get('password')
        )
        if self.user is not None:
            if not self.user.is_active:
                raise serializers.ValidationError(
                    self.error_messages['inactive_account'])
            return attrs
        else:
            raise serializers.ValidationError(
                self.error_messages['invalid_credentials'])


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ("auth_token", "created")


class UserRegisterSerializer(serializers.Serializer):

    class Meta:
        resource_name = 'register'

    username = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    default_error_messages = {
        'invalid_password': _(r"Password didn't match."),
    }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                self.error_messages['invalid_password'])
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
