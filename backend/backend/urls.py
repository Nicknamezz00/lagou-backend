from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Lagou API",
        default_version='v1',
        description="Nah",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="wrzwurunze@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include('users.urls')),
]

urlpatterns += [
    # path('openapi/',
    #      get_schema_view(
    #         title="Example API",
    #         description="API for all things …", version="1.0.0"),
    #      name='openapi-schema'),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    re_path(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
    path(
        'admin/',
        admin.site.urls),
    path(
        'api-token-auth/',
        obtain_auth_token),
]
