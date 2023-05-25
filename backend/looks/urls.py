from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('moods', views.MoodViewSet)
router.register('', views.LookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
