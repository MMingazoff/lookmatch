from django.db.models import Q
from rest_framework import viewsets, permissions

from .models import Look, Mood
from .serializers import LookSerializer, MoodSerializer


class LookViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Look.objects.all()
    serializer_class = LookSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = Look.objects.filter(Q(public=True) | Q(user=user))
        else:
            queryset = Look.objects.filter(public=True)
        return queryset


class MoodViewSet(viewsets.ModelViewSet):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer
