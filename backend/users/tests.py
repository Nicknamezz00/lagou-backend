from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):
    """
    Test suite for `AUTH_USER_MODEL`.
    """

    def setUp(self) -> None:
        self._User = get_user_model()
        # TODO: Finish this.
