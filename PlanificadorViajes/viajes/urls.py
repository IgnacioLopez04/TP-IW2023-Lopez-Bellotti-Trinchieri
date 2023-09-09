from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarViaje, name='viajes-cargar-viaje'),
    path('detalle-viaje/<int:viaje_id>/', views.detalle_viaje, name='detalle-viaje'),
]
