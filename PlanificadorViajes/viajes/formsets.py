from django.forms import formset_factory
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Viaje_Dia, Viaje_General
from .forms import CargarDiaViajeForm

class FormsetDiaViaje(FormView):
    template_name = 'dia_viaje.html'
    form_class = formset_factory(CargarDiaViajeForm, extra=1)
    success_url = reverse_lazy('sitio-inicio')
    def form_valid(self, formset):
        # Obtener el ID del viaje desde la sesión
        viaje_id = self.kwargs.get('viaje_id')
        viaje_general = Viaje_General.objects.get(id=viaje_id)

        if viaje_general:
            for f in formset:
                f_instance = f.save(commit=False)
                f_instance.viaje = viaje_general
                f_instance.save()

                destinos_seleccionados = f.cleaned_data.get('destinos')
                f_instance.destinos.set([destinos_seleccionados])  # Agregar los destinos a la relación many-to-many

                success_url.kwargs = {'id_dia_viaje':f_instance.id}

            # Actualiza el campo cantidadDias en Viaje_General
            viaje_general.cantidadDias = formset.total_form_count()
            viaje_general.save()

        return super().form_valid(formset)