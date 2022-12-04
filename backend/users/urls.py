from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('api/users', views.UserProfileViewSet, basename='users')

urlpatterns = router.urls
