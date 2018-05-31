from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet,BookViewSet,CommentViewSet,RateViewSet

route = DefaultRouter()
route.register('categories',CategoryViewSet)
route.register('books',BookViewSet)
route.register('comments',CommentViewSet)
route.register('rates',RateViewSet)

urlpatterns = [
    path('',include(route.urls)),
]