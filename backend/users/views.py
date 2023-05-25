from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets

from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = make_password(serializer.validated_data['password'])
        serializer.save(password=password)

    def perform_update(self, serializer):
        if 'password' in serializer.validated_data:
            password = make_password(serializer.validated_data['password'])
            serializer.save(password=password)
        else:
            serializer.save()


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
