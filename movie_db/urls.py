from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Movie API",
      default_version='v1',
      description="School example project",
      contact=openapi.Contact(email="superduper@teko.ch"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/v1/doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    #path('api/v1/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/', include('backend.urls')),
    path('admin/', admin.site.urls),
]
