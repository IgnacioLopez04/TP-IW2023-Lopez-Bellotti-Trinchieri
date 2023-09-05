from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from viajes.forms import ViajeForm, CargarDiaViajeForm
from viajes.models import Viaje_General, Viaje_Dia, Viaje_Dia_Destino
from django.http import HttpResponse
import random
from decimal import Decimal



@login_required
def cargarViaje(request):
    if request.method == 'POST':
        form = ViajeForm(request.POST)
        if form.is_valid():
            viaje = form.save(commit=False)  # Crea una instancia del Viaje sin guardarla aún
            viaje.usuario = request.user  # Asigna el usuario actual al campo user

            viaje.calificacion= Decimal(random.uniform(1,5)) #le doy una calificacion aleatoria por ahora para que ande el filtro
            
            viaje.save() #ahora si guarda el viaje con el usuario asignado

            viaje_id = viaje.id
            return redirect('viajes-cargar-dia-viaje', viaje_id=viaje_id)
    else:
        form = ViajeForm()

    return render(request, 'viaje.html', {'form': form})


@login_required
def cargar_dia_viaje(request): #tendria que desaparecer ya
    if request.method == 'POST':
        form = CargarDiaViajeForm(request.POST)
        if form.is_valid():
            dia_viaje = form.save()
            return redirect('viajes-cargar-dia-viaje')
    else:
        form = CargarDiaViajeForm()
    
    dia_actual = request.session.get('dia_actual', 1)
    titulo = f'Día {dia_actual}'

    return render(request, 'dia_viaje.html', {'form': form, 'titulo': titulo})


def detalle_viaje(request, viaje_id):
    viaje = get_object_or_404(Viaje_General, pk=viaje_id)
    return render(request, 'detalle-viaje.html', {'viaje': viaje})
