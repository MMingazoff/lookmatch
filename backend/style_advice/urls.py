from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('planned_looks', views.PlannedLookViewSet)
router.register('recommendations', views.RecommendationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
