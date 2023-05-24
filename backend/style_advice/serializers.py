from rest_framework import serializers

from .models import PlannedLook, Recommendation


class PlannedLookSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlannedLook
        fields = '__all__'


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'
