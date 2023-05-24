from django.db import models


class Gender(models.TextChoices):
    male = "male"
    female = "female"
    unisex = "unisex"
