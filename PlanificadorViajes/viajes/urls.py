from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarViaje, name='viajes-cargar-viaje'),
    path('detalle-viaje/<int:viaje_id>/', views.detalle_viaje, name='detalle-viaje'),
    path('detalle-viaje/<str:tk>/', views.detalle_viaje_token, name='detalle-viaje-token'),
    path('aceptarSolicitud/<str:tk>',views.aceptar_solicitud, name='aceptar-solicitud'),
    path('update/<int:viaje_pk>', views.ViajeUpdateView.as_view(), name='update-viaje'),

    path('create-dia/', views.DiaViajeCreateView, name='create-dia-viaje'),
    path('update-dia/<int:dia_pk>', views.DiaViajeUpdateView.as_view(), name='update-dia-viaje'),
    path('delete-dia/<int:dia_pk>', views.DiaViajeDeleteView.as_view(), name='delete-dia-viaje'),
    path('mostrar-dias/', views.mostrarDiasViaje, name='mostrar-dias-viaje'),
    path('confirmarViaje/', views.confirmarViaje, name='confirmar-viaje'),
]
