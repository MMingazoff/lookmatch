from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from lookmatch.settings import AUTH_USER_MODEL
from wardrobe.enums import Category
from wardrobe.models import ClothingItem


class Mood(models.Model):
    mood = models.CharField(max_length=50)

    def __str__(self):
        return self.mood


class Look(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    weather_range = IntegerRangeField()
    mood = models.ForeignKey(Mood, on_delete=models.SET_NULL, null=True)
    clothing_items = models.ManyToManyField(ClothingItem)
    date_created = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    @classmethod
    def generate_look(cls, user, weather_range, mood):
        top_item = ClothingItem.objects.filter(category=Category.top).order_by('?').first()
        bottom_item = ClothingItem.objects.filter(category=Category.bottom).order_by('?').first()
        new_look = Look.objects.create(user=user, weather_range=weather_range, mood=mood)
        new_look.clothing_items.set([top_item, bottom_item])
