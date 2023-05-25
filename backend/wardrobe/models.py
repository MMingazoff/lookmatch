from django.db import models
from lookmatch.settings import AUTH_USER_MODEL


class Color(models.Model):
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.color


class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category


class ClothingItem(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
    style = models.CharField(max_length=255)
    image = models.FileField()
    date_added = models.DateTimeField(auto_now_add=True)
