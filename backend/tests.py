from rest_framework import status
from rest_framework.test import APITestCase


class BackendTestCase(APITestCase):
    """
    Test suite for backend.
    """
    def setUp(self) -> None:
        pass

    def test_backend_is_alive(self):
        # GET testserver/
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
