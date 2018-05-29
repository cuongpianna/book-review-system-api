from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet,BookViewSet

route = DefaultRouter()
route.register('categories',CategoryViewSet)
route.register('books',BookViewSet)

urlpatterns = [
    path('',include(route.urls)),
]