# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from nubi.utils.enums.sex_type import SexType
# Django
from django.db import models


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex_type = models.CharField(
        max_length=6,
        choices=SexType.choices
    )
    dni = models.CharField(max_length=8, unique=True)
    birth_date = models.DateTimeField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )