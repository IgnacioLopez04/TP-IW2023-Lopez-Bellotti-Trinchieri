from django.urls import path, include
from . import views

urlpatterns = [
    path('cargarDestino/<int:id_dia_viaje>/<str:modal>', views.cargarDestino, name='cargar-destino'),
    path('cargarDestino/<str:modal>', views.cargarDestinoSinId, name='cargar-destino-sin-dia'),
    #path('confirmarDestino/<int:id_dia_viaje>/<str:modal>', views.confirmarDestino, name='confirmar-destino'),
]