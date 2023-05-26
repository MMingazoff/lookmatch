from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from .views import GithubLogin, GithubComplete

router = routers.DefaultRouter()
router.register('', views.UserViewSet)
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('github/login', GithubLogin.as_view(), name='github_login'),
    path('github/complete', GithubComplete.as_view(), name='github_complete'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
