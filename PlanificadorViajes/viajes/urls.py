from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarViaje, name='viajes-cargar-viaje'),
    path('cargar-dia/', views.cargarDiaViaje, name='viajes-cargar-dia-viaje'),
]
