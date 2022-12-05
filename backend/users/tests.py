from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory, RequestsClient

from coreutils.jsonapi_request import JsonAPIRequest
from coreutils.lagou_test import LagouTestUtils
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
        data = JsonAPIRequest(type='login', attrs=attrs)
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
