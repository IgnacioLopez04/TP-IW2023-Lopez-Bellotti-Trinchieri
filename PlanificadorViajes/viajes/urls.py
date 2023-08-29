from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarViaje, name='viajes-cargar-viaje'),
    path('cargar-dia/', views.cargar_dia_viaje, name='viajes-cargar-dia-viaje'),
]
