from rest_framework import viewsets

from .models import Look
from .serializers import LookSerializer


class LookViewSet(viewsets.ModelViewSet):
    queryset = Look.objects.all()
    serializer_class = LookSerializer
