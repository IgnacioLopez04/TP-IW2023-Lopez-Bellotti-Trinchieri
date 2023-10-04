from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarViaje, name='viajes-cargar-viaje'),
    path('detalle-viaje/<int:viaje_id>/', views.detalle_viaje, name='detalle-viaje'),
    path('detalle-viaje/<tk>/', views.detalle_viaje_token, name='detalle-viaje-token'),
    path('aceptarSolicitud/<str:tk>',views.aceptar_solicitud, name='aceptar-solicitud'),
]
