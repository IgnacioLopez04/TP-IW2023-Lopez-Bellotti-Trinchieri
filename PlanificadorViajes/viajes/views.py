from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from viajes.forms import ViajeForm, CargarDiaViajeForm
from django.forms import formset_factory
from viajes.models import Viaje_General, Destino, Viaje_Dia
from django.http import HttpResponse
import random
from decimal import Decimal

@login_required
def cargarViaje(request):
    DiaFormSet = formset_factory(CargarDiaViajeForm, extra=1, can_delete=True)

    if request.method == 'POST':
        # form = ViajeForm(request.POST, meses_dict = meses_dict)
        viaje_form = ViajeForm(request.POST)
        dia_formset = DiaFormSet(request.POST)

        if viaje_form.is_valid():
            viaje_form = viaje_form.save(commit=False)
            viaje_form.usuario = request.user

            viaje_form.calificacion= random.randint(1, 5) #le doy una calificacion aleatoria por ahora para que ande el filtro
            viaje_form.save()


        if dia_formset.is_valid():
            cant_dias = 0

            for f in dia_formset:
                if f in dia_formset.deleted_forms:
                    continue
                f_instance = f.save(commit=False)
                f_instance.viaje = viaje_form
                f_instance.save()

                cant_dias += 1
                
                destinos_seleccionados = f.cleaned_data['destinos']
                f_instance.destinos.set([destinos_seleccionados])  # Agregar los destinos a la relación many-to-many

            viaje_form.cantidadDias = cant_dias
            viaje_form.save()

            return redirect('sitio-inicio')
    else:
        viaje_form = ViajeForm()
        dia_formset = DiaFormSet()

    return render(request, 'viaje.html', {
        'form': viaje_form,
        'formset': dia_formset,
    })


def detalle_viaje(request, viaje_id):
    viaje = get_object_or_404(Viaje_General, pk=viaje_id)
    return render(request, 'detalle-viaje.html', {'viaje': viaje})
