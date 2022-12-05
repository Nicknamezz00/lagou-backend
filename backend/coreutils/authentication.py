from rest_framework.authentication import BaseAuthentication


class AnyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        return
