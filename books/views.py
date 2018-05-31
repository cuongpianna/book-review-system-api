from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter

from .permisions import IsAdminOrReadOnly,IsOwnerOrReadOnly
from .serializers import BookSerializer,CategorySerialzer,CommentSerializer,RateSerializer
from .models import Book,Category,Comment,Rate

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CategorySerialzer
    filter_backends = (DjangoFilterBackend,)



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter,SearchFilter)
    filter_fields = ('author','category')
    search_fields = ('author','title','category__name')
    ordering_fields = ('author',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = (IsOwnerOrReadOnly,IsAuthenticated)
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('text','owner','book')
    search_fields = ('text',)

class RateViewSet(ModelViewSet):
    queryset = Rate.objects.all()
    permission_classes = (IsOwnerOrReadOnly,IsAuthenticated)
    serializer_class = RateSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('owner',)



