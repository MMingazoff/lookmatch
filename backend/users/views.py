from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
