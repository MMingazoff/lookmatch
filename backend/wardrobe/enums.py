from django.db import models


class Category(models.TextChoices):
    top = "top"
    bottom = "bottom"


class Color(models.TextChoices):
    black = "black"
    white = "white"
