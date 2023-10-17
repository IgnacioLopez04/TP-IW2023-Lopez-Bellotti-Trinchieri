from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from viajes.models import Viaje_General, Viaje_Dia
import json
from django.http import JsonResponse
from django.conf import settings

@login_required
def cargarDestino(request, id_dia_viaje):
    return render(request, 'cargarDestino.html', {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY})

def confirmarDestino(request, id_dia_viaje):
    if request.method == 'POST':
        dia_viaje = get_object_or_404(Viaje_Dia, id = id_dia_viaje)
        try:
            data = json.loads(request.body.decode('utf-8'))
            destinos = data['destinos']
            for destino in destinos:
                dia_viaje.destinos.create(nombre=destino)
            
            dia_viaje.save()
            
            response_data = {
                'message': 'Los destinos fueron cargados.'
            }
            
            return JsonResponse(response_data)
        except json.JSONDecodeError as e:
            response_data = {'error': 'Error en los datos JSON: ' + str(e)}
            return JsonResponse(response_data, status=400)  # Devuelve una respuesta de error

