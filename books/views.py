from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .permisions import IsAdminOrReadOnly,IsOwnerOrReadOnly

from .serializers import BookSerializer,CategorySerialzer
from .models import Book,Category

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = CategorySerialzer



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (IsOwnerOrReadOnly,IsAuthenticated)
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



