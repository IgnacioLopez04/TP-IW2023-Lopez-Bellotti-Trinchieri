from django.urls import path
from . import views
from .formsets import FormsetDiaViaje

urlpatterns = [
    path('', views.cargarViaje, name='viajes-cargar-viaje'),

    #FORMSET
    path('cargar-dia/', FormsetDiaViaje.as_view(), name='viajes-cargar-dia-viaje'),
]
