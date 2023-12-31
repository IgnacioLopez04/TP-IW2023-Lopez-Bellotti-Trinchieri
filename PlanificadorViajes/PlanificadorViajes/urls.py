"""
URL configuration for PlanificadorViajes project.

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
from SitioWeb import views
from django.views.generic.base import TemplateView
from django.conf import settings
# esto deberia cambiarse pq sirve para desarrollo
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('sitio/', include('SitioWeb.urls')),
    path('viajes/', include('viajes.urls')),
    path('registration/', include('registration.urls')),
    path('api/', include('apis.urls')),
    path('googleMaps/', include('googleMaps.urls')),
    path('', include('allauth.urls')),
    path('rebuild_index/', views.rebuild_index),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

# Solo anda en desarrollo, en produccion deberiamos montar otra cosa, como NGNEX
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
