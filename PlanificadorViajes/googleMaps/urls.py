from django.urls import path, include
from . import views

urlpatterns = [
    path('cargarDestino/<int:id_dia_viaje>', views.cargarDestino, name='cargar-destino'),
    # path('confirmarDestino/<int:id_dia_viaje>', views.confirmarDestino, name='confirmar-destino'),
]