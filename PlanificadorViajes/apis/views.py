from django.shortcuts import render
from django.http import HttpResponse
from viajes.models import Viaje_General

def api_viajes(request): #Api para mostrar los viajes que hay cargados
    viajes = Viaje_General.objects.order_by('nombreViaje')
    return render(request, 'api_viajes.html', {'lista_viajes':viajes})
