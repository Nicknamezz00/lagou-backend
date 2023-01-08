from django.utils.translation import gettext_lazy as _
from django.db import models
from django_extensions.db.fields import RandomCharField
from coreutils.abstract_models import Model


class Company(Model):

    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('companies')

    class JSONAPIMeta:
        resource_name = 'companies'

    name = models.CharField()


class WebSource(Model):

    class Meta:
        verbose_name = _('web source')
        verbose_name_plural = _('web source')

    class JSONAPIMeta:
        resource_name = 'websources'

    url = models.URLField(_('url'), default='')


class Job(Model):

    class Meta:
        verbose_name = _('job')
        verbose_name_plural = _('jobs')

    class JSONAPIMeta:
        resource_name = 'jobs'

    SPECIALTY = 'SP'
    UNDERGRADUATE = 'UN'
    MASTER = 'MA'
    DOCTOR = 'DO'

    EDU_BACKGROUND_CHOICES = [
        (SPECIALTY, '大专'),
        (UNDERGRADUATE, '本科'),
        (MASTER, '硕士'),
        (DOCTOR, '博士')
    ]

    FRESH = 'FR'
    LESS_THAN_THREE_YEARS = 'LE'
    THREE_TO_FIVE_YEARS = 'TH'
    FIVE_TO_TEN_YEARS = 'FI'
    MORE_THAN_TEN_YEARS = 'MO'

    EXPERIENCE_CHOICES = [
        (FRESH, (0, 0)),
        (LESS_THAN_THREE_YEARS, (0, 3)),
        (THREE_TO_FIVE_YEARS, (3, 5)),
        (FIVE_TO_TEN_YEARS, (5, 10)),
        (MORE_THAN_TEN_YEARS, (10, 10)),
    ]

    name = models.CharField(_('job_name'), max_length=128)
    salary = models.CharField(_('salary'), max_length=16, default='0')
    headcount = models.IntegerField(_('headcount'), default=0)
    edu_background = models.Choices(EDU_BACKGROUND_CHOICES)
    experience = models.Choices(EXPERIENCE_CHOICES)
