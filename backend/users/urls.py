from django.urls import path, include
from rest_framework import routers

from . import views
from .views import RegisterView

router = routers.DefaultRouter()
router.register('', views.UserViewSet)
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view()),
]
