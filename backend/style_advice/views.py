from rest_framework import viewsets

from .models import PlannedLook, Recommendation
from .serializers import PlannedLookSerializer, RecommendationSerializer


class PlannedLookViewSet(viewsets.ModelViewSet):
    queryset = PlannedLook.objects.all()
    serializer_class = PlannedLookSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
