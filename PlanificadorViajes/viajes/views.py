from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from viajes.forms import ViajeForm, CargarDiaViajeForm
from django.forms import formset_factory
from viajes.models import Viaje_General, Destino, Viaje_Dia
from django.http import HttpResponse
import random
from decimal import Decimal
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model
from registration.token import account_activation_token, account_activation_token_viaje 
from django.contrib import messages
import json
from django.http import JsonResponse

### PRUEBA ###
from viajes.forms import DiaViajeForm
@login_required
def cargarViaje(request):
    DiaFormSet = formset_factory(CargarDiaViajeForm, extra=1, can_delete=True)

    correos = []
    
    if request.method == 'POST':
        # form = ViajeForm(request.POST, meses_dict = meses_dict)
        viaje_form = ViajeForm(request.POST)
        dia_formset = DiaFormSet(request.POST)

        if viaje_form.is_valid():
            viaje_form = viaje_form.save(commit=False)
            viaje_form.usuario = request.user

            viaje_form.calificacion= random.randint(1, 5) #le doy una calificacion aleatoria por ahora para que ande el filtro

            viaje_form.token = account_activation_token_viaje.make_token(viaje_form.usuario)
            for key in request.POST.keys():
                if key.startswith('correo-span'):
                    print(key)
                    correo = request.POST.get(key, '')
                    correos.append(correo)
            
            for correo in correos:
                enviar_correos_privados(request,correo,viaje_form.token)
            viaje_form.save()


        #ver si el viaje es privado y si hay correos para enviar (puede ser que sea privado y no quiera invitar a nadie)
        es_privado = viaje_form.esPrivado
        
        if dia_formset.is_valid():
            cant_dias = 0

            for f in dia_formset:
                if f in dia_formset.deleted_forms:
                    continue
                f_instance = f.save(commit=False)
                f_instance.viaje = viaje_form
                f_instance.save()

                cant_dias += 1

                destinos_seleccionados = f.cleaned_data.get('destinos')
                f_instance.destinos.set([destinos_seleccionados])

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
    
    if request.user == viaje.usuario:
        
        if request.method == 'POST':
            correo = request.POST.get('correo', '')
            if correo:
                enviar_correos_privados(request,correo,viaje.token)
        
        return render(request, 'detalle-viaje.html', {'viaje': viaje})
    else:
        messages.error(request, f'El viaje es privado. No tenes acceso.')
        return redirect('sitio-inicio')

def detalle_viaje_token(request, tk):
    viaje = get_object_or_404(Viaje_General, token=tk)
    
    if viaje is not None:
        return render(request, 'detalle-viaje.html', {'viaje': viaje})
    else:
        messages.error(request, f'No se encontro el viaje.')
        return redirect('sitio-inicio')

def aceptar_solicitud(self, tk):
    try:
        viaje = get_object_or_404(Viaje_General, token = tk)
    except:
        viaje = None
    # if viaje is not None and account_activation_token_viaje.check_token(viaje, tk): Esto no funciona, pero deberia funcionar xd
        # return redirect('detalle-viaje-token', tk = tk)
    return redirect('detalle-viaje-token', tk = tk)
    

def enviar_correos_privados(request, to_email, token):
    
    mail_subject = 'Invitacion a un viaje privado en Los Tres Viajeros'
    messages_content = render_to_string('invitacion_mail.html',{
        'domain': get_current_site(request).domain,
        'token': token,
        'protocol': 'https' if request.is_secure() else 'http'
    })
    
    email = EmailMessage(mail_subject, messages_content, to=[to_email])
    if email.send():
        messages.success(request, f'La invitacion fue enviada.')
    else:
        messages.error(request, f'No envie el mail') 

### PRUEBA DEL NUEVO CARGAR VIAJE ###

@login_required
def cargarViaje_prueba_(request):
    correos = []

    if request.method == 'POST':
        viaje_form = ViajeForm(request.POST)
        dia_form = DiaViajeForm(request.POST)

        if viaje_form.is_valid():
            viaje_form = viaje_form.save(commit=False)
            viaje_form.usuario = request.user

            viaje_form.calificacion = random.randint(1, 5)  # le doy una calificacion aleatoria por ahora para que ande el filtro

            viaje_form.token = account_activation_token_viaje.make_token(viaje_form.usuario)
            for key in request.POST.keys():
                if key.startswith('correo-span'):
                    print(key)
                    correo = request.POST.get(key, '')
                    correos.append(correo)

            for correo in correos:
                enviar_correos_privados(request, correo, viaje_form.token)
            viaje_form.save()

        # ver si el viaje es privado y si hay correos para enviar (puede ser que sea privado y no quiera invitar a nadie)
        es_privado = viaje_form.esPrivado

        if dia_form.is_valid():
            cant_dias = 0

            for f in dia_form:
                if f in dia_form.deleted_forms:
                    continue
                f_instance = f.save(commit=False)
                f_instance.viaje = viaje_form
                f_instance.save()

                cant_dias += 1

            viaje_form.cantidadDias = cant_dias
            viaje_form.save()

            return redirect('cargar-dia-viaje')
    else:
        viaje_form = ViajeForm()
        dia_form = DiaViajeForm()

    dias_viaje = Viaje_Dia.objects.all() # filtrar y devolver solo los de ese dia
    # por ahora devuelvo todos para testear

    return render(request, 'nuevo_viaje.html', {
        'dias_viaje' : dias_viaje,
        'viaje_form': viaje_form,
        'dia_form': dia_form,
    })

from django.urls import reverse_lazy
from django.views import generic
from .forms import DiaViajeForm
from .models import Viaje_Dia
from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)
class Index(generic.ListView):
    model = Viaje_Dia
    context_object_name = 'dias_viaje'
    template_name = 'nuevo_viaje.html'

#CREAR
class DiaViajeCreateView(BSModalCreateView):
    template_name= 'CRUD-dia-viaje/crear-dia-viaje.html'
    form_class = DiaViajeForm
    success_message = 'El dia fue cargado con exito!'
    success_url = reverse_lazy('cargar-viaje-prueba')

#ACTUALIZAR
class DiaViajeUpdateView(BSModalUpdateView):
    model = Viaje_Dia
    template_name = 'CRUD-dia-viaje/actualizar-dia-viaje.html'
    form_class = DiaViajeForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('cargar-viaje-prueba')

# LEER
class DiaViajeReadView(BSModalReadView):
    model = Viaje_Dia
    template_name = 'CRUD-dia-viaje/leer-dia-viaje.html'

# ELIMINAR
class DiaViajeDeleteView(BSModalDeleteView):
    model = Viaje_Dia
    template_name = 'CRUD-dia-viaje/eliminar-dia-viaje.html'
    success_message = 'El dia fue eliminado con exito!'
    success_url = reverse_lazy('cargar-viaje-prueba')