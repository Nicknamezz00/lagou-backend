from django.utils.translation import gettext_lazy as _
from django.db import models
from django_extensions.db.fields import RandomCharField
from coreutils.abstract_models import Model


class Job(Model):

    class Meta:
        verbose_name = _('job')
        verbose_name_plural = _('jobs')

    class JSONAPIMeta:
        resource_name = 'jobs'

    job_name = RandomCharField(
        _('job_name'),
        length=8,
        unique=True
    )
    salary = models.IntegerField(
        _('salary'),
        default=0,
    )
    headcount = models.IntegerField(
        _('headcount'),
        default=0,
    )
    education = models.Choices()
    experience = models.Choices()
