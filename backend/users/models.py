import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _


def upload_avatar_to(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        "avatar_images",
        "avatar_{uuid}_{filename}{ext}".format(
            uuid=uuid.uuid4(), filename=filename, ext=ext
        ),
    )


class UserProfile(models.Model):

    class Meta:
        verbose_name = _("user profile")
        verbose_name_plural = _("user profiles")

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='lagou_userprofile',
    )

    preferred_language = models.CharField(
        verbose_name=_("preferred language"),
        max_length=10,
        help_text=_("Select language for the admin"),
        default="",
    )

    avatar = models.ImageField(
        verbose_name=_("profile picture"),
        upload_to=upload_avatar_to,
        blank=True,
    )

    def get_preferred_language(self):
        return self.preferred_language or get_language()

    @classmethod
    def get_for_user(cls, user):
        return cls.objects.get_or_create(user=user)[0]

    def __str__(self):
        return self.user.get_username()
