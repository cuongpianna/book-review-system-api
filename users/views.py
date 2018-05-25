from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets,permissions,mixins
from rest_framework.generics import CreateAPIView

from .models import Profile
from .serializers import UserSerializer,ProfileSerializer,UserCreateSerializer
from .permisions import IsOwnerOrReadOnly,IsSameUserAllowEditionOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsSameUserAllowEditionOrReadOnly)

class CreateUserView(CreateAPIView):
    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserCreateSerializer


