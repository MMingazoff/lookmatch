from django.db import models


class Mood(models.TextChoices):
    good = "good"
    bad = "bad"
