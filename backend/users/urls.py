from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('api/users', views.UserProfileViewSet, basename='users')

urlpatterns = router.urls

urlpatterns += [
    path(r'api/login/', views.UserLoginAPIView.as_view(), name='login'),
    path(r'api/register/', views.UserRegisterAPIView.as_view(), name='register')
]
