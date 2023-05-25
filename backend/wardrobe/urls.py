from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('colors', views.ColorViewSet)
router.register('categories', views.CategoryViewSet)
router.register('', views.ClothingItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
