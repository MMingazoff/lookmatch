from rest_framework import serializers
from wardrobe.models import ClothingItem

from .models import Look, Mood


class LookSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    clothing_items = serializers.PrimaryKeyRelatedField(many=True, queryset=ClothingItem.objects.all())

    class Meta:
        model = Look
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['clothing_items'] = [
            item.image.url
            for item in instance.clothing_items.all()
        ]
        representation['mood'] = instance.mood.mood
        return representation


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'
