from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory, RequestsClient

from coreutils.jsonapi_request import json_api_request
from coreutils.test_utils import LagouTestUtils, rsg
from users.models import UserProfile


class UserTestCase(APITestCase, LagouTestUtils):
    """
    Test suite for `AUTH_USER_MODEL`.
    """

    def setUp(self) -> None:
        self._User = get_user_model()
        self.NUMBER_OF_USERS = 5
        self.TEST_USERNAME = 'TestUser'
        self.users = [
            self.create_user(
                username=f'{self.TEST_USERNAME}{ind}',
                password=f'{self.TEST_USERNAME}{ind}'
            ) for ind in range(self.NUMBER_OF_USERS)
        ]

    def test_setUp(self):
        for user in self.users:
            self.assertIsNotNone(
                self._User.objects.get(username=user.username),
                msg=f'Did not find {user.username}!')

    def test_user_token_generated(self):
        for user in self.users:
            self.assertIsNotNone(
                Token.objects.get(user=user),
                msg=f'Did not find auto token for {user.username}!')

    def test_user_profile_generated(self):
        for user in self.users:
            self.assertIsNotNone(
                UserProfile.objects.get(user=user),
                msg=f'Did not find profile for {user.username}!')

    def test_casade(self):
        u = self.create_user(
            username='test_cascade',
            password='test_cascade'
        )
        self._User.objects.get(username='test_cascade').delete()
        self.assertEqual(
            self._User.objects.filter(username='test_cascade').count(), 0)
        self.assertEqual(
            Token.objects.filter(user__username='test_cascade').count(), 0)


class UserLoginAPIViewTestCase(APITestCase, LagouTestUtils):

    def setUp(self) -> None:
        self.url = reverse('login')
        self.username = 'David'
        self.password = 'DavidDavid'
        self.user = self.create_user(
            username=self.username,
            password=self.password
        )
        self.factory = APIRequestFactory()
        self.requestsClient = RequestsClient()

    def test_login(self):
        attrs = {
            "username": self.username,
            "password": self.password
        }
        data = json_api_request(resource='login', attrs=attrs)
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserRegisterAPIViewTestCase(APITestCase, LagouTestUtils):
    def setUp(self) -> None:
        self.resource = 'register'
        self.url = reverse('register')
        self.username = f'register_user_{rsg()}'
        self.password = f'register_user_{rsg()}'

    def test_register(self):
        attrs = {
            "username": self.username,
            "password": self.password,
            "password2": self.password
        }
        data = json_api_request(resource=self.resource, attrs=attrs)
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(User.objects.get(username=self.username).count(), 1)
