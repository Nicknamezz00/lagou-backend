from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from users.models import UserProfile


@receiver(signal=post_save,
          sender=settings.AUTH_USER_MODEL,
          weak=False)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(signal=post_save,
          sender=settings.AUTH_USER_MODEL,
          weak=False)
def create_default_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
