from django.contrib.auth.models import AbstractUser
from django.db import models
from lookmatch.settings import AUTH_USER_MODEL

from .enums import Gender


class User(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    location = models.CharField(max_length=255, null=True, blank=True)
