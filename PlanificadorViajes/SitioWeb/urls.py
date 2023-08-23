from django.urls import path, include
from SitioWeb import views

urlpatterns = [
    path('', views.inicio, name='sitio-inicio'),
    path('cargar-viaje/', include('viajes.urls')),
]