from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from .models import ClothingItem, Color, Category
from .serializers import ClothingItemSerializer, ColorSerializer, CategorySerializer


class ClothingItemViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ClothingItemSerializer
    queryset = ClothingItem.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'user', 'color', 'category']
    http_method_names = ['get', 'post', 'patch', 'delete']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return ClothingItem.objects.filter(user=self.request.user)


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
