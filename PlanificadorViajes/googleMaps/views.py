from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from viajes.models import Viaje_General, Viaje_Dia
import json
from django.http import JsonResponse
from django.conf import settings

@login_required
def cargarDestino(request, id_dia_viaje, modal):
    return render(request, 'cargarDestino.html', {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY})
@login_required
def cargarDestinoSinId(request, modal):
    return render(request, 'cargarDestino.html', {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY})

