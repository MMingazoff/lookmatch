from django.db import models
from lookmatch.settings import AUTH_USER_MODEL

from .enums import Category, Color


class ClothingItem(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(choices=Category.choices, max_length=40)
    color = models.CharField(choices=Color.choices, max_length=20)
    style = models.CharField(max_length=255)
    image = models.FileField()
    date_added = models.DateTimeField(auto_now_add=True)
