from django.utils.translation import gettext_lazy as _

from django.db import models


class SexType(models.TextChoices):
    FEMALE = 'female', _('Female')
    MALE = 'male', _('Male')
