from django.forms import formset_factory
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Viaje_Dia
from .forms import DiaViajeForm

class FormsetDiaViaje(FormView):
    template_name = 'dia_viaje.html'
    form_class = formset_factory(DiaViajeForm, extra=1)
    succes_url = reverse_lazy('#')

    def form_valid(self, form):
        for f in form:
            if f.is_valid():
                #f.save()
                print(f)
        return super().form_valid(form)