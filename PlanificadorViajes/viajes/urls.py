from django.urls import path
from . import views
from .formsets import FormsetDiaViaje

urlpatterns = [
    path('', views.cargarViaje, name='viajes-cargar-viaje'),
    #FORMSET
    path('cargar-dia/<int:viaje_id>/', FormsetDiaViaje.as_view(), name='viajes-cargar-dia-viaje'),
    path('detalle-viaje/<int:viaje_id>/', views.detalle_viaje, name='detalle-viaje'),
]
