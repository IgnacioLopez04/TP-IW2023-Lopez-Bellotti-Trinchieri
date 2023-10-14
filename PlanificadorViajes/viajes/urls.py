from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarViaje, name='viajes-cargar-viaje'),
    path('detalle-viaje/<int:viaje_id>/', views.detalle_viaje, name='detalle-viaje'),
    path('detalle-viaje/<tk>/', views.detalle_viaje_token, name='detalle-viaje-token'),
    path('aceptarSolicitud/<str:tk>',views.aceptar_solicitud, name='aceptar-solicitud'),

    ### PRUEBA ###

    path('create/', views.DiaViajeCreateView, name='create-dia-viaje'),
    path('update/<int:dia_pk>', views.DiaViajeUpdateView.as_view(), name='update-dia-viaje'),
    path('read/<int:dia_pk>', views.DiaViajeReadView.as_view(), name='read-dia-viaje'),
    path('delete/<int:dia_pk>', views.DiaViajeDeleteView.as_view(), name='delete-dia-viaje'),
]
