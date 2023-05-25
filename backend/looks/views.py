from rest_framework import viewsets, permissions

from .models import Look, Mood
from .serializers import LookSerializer, MoodSerializer


class LookViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Look.objects.all()
    serializer_class = LookSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MoodViewSet(viewsets.ModelViewSet):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer
