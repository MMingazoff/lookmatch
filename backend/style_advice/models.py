from django.db import models
from lookmatch.settings import AUTH_USER_MODEL
from looks.models import Look


class PlannedLook(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    look = models.ForeignKey(Look, on_delete=models.CASCADE)
    planned_date = models.DateField()
    notes = models.TextField(blank=True)


class Recommendation(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.FileField()
    date_published = models.DateTimeField(auto_now_add=True)
