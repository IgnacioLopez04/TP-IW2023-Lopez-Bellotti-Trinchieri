from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from viajes.forms import ViajeForm, CargarDiaViajeForm
from viajes.models import Viaje_General
from django.http import HttpResponse


@login_required
def cargarViaje(request):
    if request.method == 'POST':
        form = ViajeForm(request.POST)
        if form.is_valid():
            viaje = form.save(commit=False)  # Crea una instancia del Viaje sin guardarla aún
            viaje.usuario = request.user  # Asigna el usuario actual al campo user
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