"""
URL configuration for dyingearthcode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from dashboard import api
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Dyingearth",
      default_version="v1",
      description="Dyingearth Api Documentaion",
      terms_of_service="https://dyingearth.com/policies/terms/",
      contact=openapi.Contact(email="contact@dyinearth.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
)
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("", include("dashboard.urls"), name='Dashboard'),
    path('accounts/', include('allauth.urls')),
    path('api/', include('dashboard.api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
