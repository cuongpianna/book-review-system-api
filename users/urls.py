from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserViewSet,ProfileViewSet,CreateUserView,LoginView

router = DefaultRouter()
router.register('users',UserViewSet)
router.register('profiles',ProfileViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('register/', CreateUserView.as_view()),
    path('login/',LoginView.as_view(),name='login'),
]
