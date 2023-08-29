from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from viajes.forms import ViajeForm, CargarDiaViajeForm

@login_required
def cargarViaje(request):
    if request.method == 'POST':
        form = ViajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viajes-cargar-dia-viaje')
    else:
        form = ViajeForm()

    return render(request, 'viaje.html', {'form': form})

"""@login_required
def cargarDiaViaje(request):
    if request.method == 'POST':
        form = DiaViajeForm(request.POST)
        if form.is_valid():
            dia_actual = request.session.get('dia_actual', 1)
            form.save()
            dia_actual += 1
            request.session['dia_actual'] = dia_actual
            request.session.save()
            return redirect('viajes-cargar-dia-viaje')
    else:
        form = DiaViajeForm()

    dia_actual = request.session.get('dia_actual', 1)
    titulo = f'Día {dia_actual}'
    return render(request, 'dia_viaje.html', {'form': form, 'titulo': titulo})"""

@login_required
def cargar_dia_viaje(request):
    if request.method == 'POST':
        form = CargarDiaViajeForm(request.POST)
        if form.is_valid():
            dia_viaje = form.save()
            destinos_seleccionados = form.cleaned_data['destinos']
            dia_viaje.destinos.set(destinos_seleccionados)
            return redirect('viajes-cargar-dia-viaje')
    else:
        form = CargarDiaViajeForm()
    
    dia_actual = request.session.get('dia_actual', 1)
    titulo = f'Día {dia_actual}'
    return render(request, 'dia_viaje.html', {'form': form, 'titulo': titulo})