from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from requests import Response
from requests.exceptions import HTTPError
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from social_core.exceptions import MissingBackend, AuthTokenError
from social_django.utils import load_strategy, load_backend

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


redirect_url = ''


class GithubLogin(APIView):
    def get(self, request):
        strategy = load_strategy(request)
        global redirect_url
        redirect_url = request.GET.get('redirect_to')
        backend = load_backend(strategy=strategy, name='github', redirect_uri="/api/users/github/complete")

        url = backend.auth_url()
        return redirect(url)


class GithubComplete(APIView):
    def get(self, request):
        strategy = load_strategy(request)
        backend = load_backend(strategy=strategy, name='github', redirect_uri="")

        try:
            user_social_auth = backend.complete(request=request)
            print(user_social_auth)
            refresh = RefreshToken.for_user(user_social_auth)

            # Parse the URL
            parsed_url = urlparse(redirect_url)

            # Get the existing query parameters as a dictionary
            query_params = dict(parse_qsl(parsed_url.query))

            # Add or update the query parameters
            query_params['access'] = str(refresh.access_token)
            query_params['refresh'] = str(refresh)

            # Encode the updated query parameters
            encoded_query_params = urlencode(query_params)

            # Update the query component of the parsed URL
            updated_url = urlunparse(parsed_url._replace(query=encoded_query_params))

            return redirect(updated_url)

        except (MissingBackend, AuthTokenError, HTTPError):
            return Response({'errors': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
