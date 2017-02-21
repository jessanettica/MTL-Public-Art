from django.db import models
from django.contrib.auth.models import AbstractUser

from mtlartsite import settings


class User(AbstractUser):
    city = models.CharField(max_length=100, blank=True)
