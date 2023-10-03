from django.urls import path, include
from . import views

urlpatterns = [
    path('cargarDestino/<int:numDia>', views.cargarDestino, name='cargar-destino'),
]