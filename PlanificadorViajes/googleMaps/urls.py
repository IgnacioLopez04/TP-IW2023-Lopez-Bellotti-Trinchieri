from django.urls import path, include
from . import views

urlpatterns = [
    path('cargarDestino/', views.cargarDestino, name='cargar-destino'),
]