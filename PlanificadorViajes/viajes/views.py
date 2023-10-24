from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from viajes.forms import ViajeForm, CargarDiaViajeForm
from viajes.models import Viaje_General, Viaje_Dia
import random

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from registration.token import account_activation_token_viaje 
from django.contrib import messages
import json

from django.core import serializers
from django.http import JsonResponse
from django.urls import reverse_lazy

from .forms import CargarDiaViajeForm
from .models import Viaje_Dia
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.detail import DetailView

def detalle_viaje(request, viaje_id): 
    viaje_actual = get_object_or_404(Viaje_General, pk=viaje_id)
    dias_viaje = Viaje_Dia.objects.filter(viaje = viaje_actual)
    if request.user == viaje_actual.usuario:
        if request.method == 'POST':
            correo = request.POST.get('correo', '')
            if correo:
                enviar_correos_privados(request,correo,viaje_actual.token)
        
        return render(request, 'detalle-viaje.html', {'viaje': viaje_actual, 'imagen_dia': dias_viaje, 'GOOGLE_API_KEY': settings.GOOGLE_API_KEY, 'correo': True})
    else:
        return render(request, 'detalle-viaje.html', {'viaje': viaje_actual, 'imagen_dia': dias_viaje, 'GOOGLE_API_KEY': settings.GOOGLE_API_KEY, 'correo': False})
        
def detalle_viaje_token(request, tk):
    viaje = get_object_or_404(Viaje_General, token=tk)
    dias_viaje = get_object_or_404(Viaje_Dia, viaje = viaje)
    
    if viaje  is not None:
        return render(request, 'detalle-viaje.html', {'viaje': viaje , 'GOOGLE_API_KEY': settings.GOOGLE_API_KEY})
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
        messages.error(request, f'No envie el mail.') 

###########

def buscarCorreo(request, viaje):
    correos = []
    viaje.token = account_activation_token_viaje.make_token(viaje.usuario)
    for key in request.POST.keys():
        if key.startswith('correo-span'):
            print(key)
            correo = request.POST.get(key, '')
            correos.append(correo)

    for correo in correos:
        enviar_correos_privados(request, correo, viaje.token)

@login_required
def cargarViaje(request):

    if request.method == 'POST':
        viaje_form = ViajeForm(request.POST, request.FILES)

        if viaje_form.is_valid():
            viaje_form = viaje_form.save(commit=False)
            viaje_form.usuario = request.user

            viaje_form.calificacion = random.randint(1, 5)  # le doy una calificacion aleatoria por ahora para que ande el filtro
            
            buscarCorreo(request, viaje_form)
            viaje_form.estado = 'BORRADOR'

            
            dias_viaje = Viaje_Dia.objects.filter(viaje = viaje_form.id)               

            viaje_form.cantidadDias= dias_viaje.count()
          
            viaje_form.save()

            response_data = {
                'success': True,
                'message': 'Los datos del viaje han sido guardados con éxito.',
                'id_viaje': viaje_form.id,
            }

            return JsonResponse(response_data)
    else:
        viaje_form = ViajeForm()

    
    # filtrar y devolver solo los de ese dia
    # por ahora devuelvo todos para testear
    dias_viaje = ''
    dia_form = CargarDiaViajeForm()
    return render(request, 'viaje.html', {
        'dias_viaje' : dias_viaje,
        'viaje_form': viaje_form,
        'dia_form' : dia_form,
     })
    
def confirmarViaje(request):
    response_data = {}
    
    if request.method == "POST":
        id_viaje = request.POST.get('id-viaje')
        if id_viaje == '':
            messages.error(request, f'Se necesita tener al menos cargado un dia del viaje.')
            response_data['success'] = False
            
        else:
            viaje_actual = get_object_or_404(Viaje_General, pk = id_viaje)
            
            viaje_actual.estado = "ACTIVO"
            viaje_actual.cantidadDias = viaje_actual.viaje_dia.count()
            viaje_actual.save()
            messages.success(request, f'Se confirmo el viaje.')
            response_data['success'] = True
            
            buscarCorreo(request, viaje_actual)
           
        messages_list = [str(message) for message in messages.get_messages(request)]
        response_data['messages'] = messages_list
        
        
        return JsonResponse(response_data)

#CREAR
def DiaViajeCreateView(request):
    id_viaje = request.POST.get('id-viaje')
    destinos = request.POST.getlist('input-destino')
    viaje_general = get_object_or_404(Viaje_General, id=id_viaje)

    if request.method == 'POST':
        dia_form = CargarDiaViajeForm(request.POST, request.FILES)
        if dia_form.is_valid():
            dia = dia_form.save(commit=False)
            dia.viaje = viaje_general
            dia.save()

            destinos_fomateados = []
            for destino in destinos:
                ciudad, provincia, latitud, longitud = destino.split(", ")
                destino_fomateado = {
                    'nombre' : ciudad,
                    'provincia' : provincia,
                    'latitud' : latitud,
                    'longitud' : longitud,
                }

                destinos_fomateados.append(destino_fomateado)

            destinos_json = json.dumps(destinos_fomateados)

            dia.destinos = destinos_json

            dia.save()

            response_data = {
                'success': True,
                'message': 'Los datos del dia han sido guardados con éxito.',
            }

            return JsonResponse(response_data)
#ACTUALIZAR
class DiaViajeUpdateView(UpdateView):
    model = Viaje_Dia
    template_name = 'CRUD-dia-viaje/actualizar-dia-viaje.html'
    form_class = CargarDiaViajeForm
    success_message = 'El dia fue actualizado con exito!.'
    success_url = reverse_lazy('viajes-cargar-viaje')

    def get_object(self):
        dia_pk = self.kwargs['dia_pk']
        return get_object_or_404(self.model, pk=dia_pk)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        viaje = obj.viaje
        viaje_actual = get_object_or_404(Viaje_General, id=viaje.id)

        obj_POST = request.POST
        obj.nombreDia = obj_POST['nombreDia']
        obj.notas = obj_POST['notas']
        #faltaria el resto de campos
        obj.save()

        dias_viaje = Viaje_Dia.objects.filter(viaje=viaje_actual)

        print("dias viaje: ", dias_viaje)

        response_data = {
            'html_response' : render_to_string('mostrar-dias-viaje.html', {'dias_viaje': dias_viaje})
        }

        return JsonResponse(response_data)

# ELIMINAR
class DiaViajeDeleteView(DeleteView):
    model = Viaje_Dia
    template_name = 'CRUD-dia-viaje/eliminar-dia-viaje.html'
    success_message = 'El dia fue eliminado con exito!.'
    success_url = reverse_lazy('viajes-cargar-viaje')

    def get(self, request, dia_pk, *args, **kwargs):
        dia_viaje = get_object_or_404(Viaje_Dia, pk=dia_pk)
        return render(request, self.template_name, {'dia': dia_viaje})

    def get_object(self):
        dia_pk = self.kwargs['dia_pk']
        return get_object_or_404(self.model, pk=dia_pk)

    def delete(self, request, *args, **kwargs):
        dia_pk = self.kwargs['dia_pk']
        dia = get_object_or_404(Viaje_Dia, pk=dia_pk)
        dia.delete()

        response = {
            'success': True,
            'message': 'El día fue eliminado con éxito.',
        }

        return JsonResponse(response)
    
# Mostrar dias viaje
def mostrarDiasViaje(request):
    id_viaje = request.POST.get('id-viaje')
    viaje_actual = get_object_or_404(Viaje_General, id = id_viaje)
    dias_viaje = Viaje_Dia.objects.filter(viaje=viaje_actual)

    response = {
        'html_response': render_to_string('mostrar-dias-viaje.html', {'dias_viaje': dias_viaje}),
    }
    
    return JsonResponse(response)

class ViajeUpdateView(UpdateView):
    model = Viaje_General
    template_name = 'viaje.html'
    form_class = ViajeForm
    success_message = 'El viaje fue actualizado con exito!.'
    success_url = reverse_lazy('viajes-cargar-viaje')

    def get_object(self):
        viaje_pk = self.kwargs['viaje_pk']
        return get_object_or_404(self.model, pk=viaje_pk)

    def get_context_data(self, **kwargs):
        dia_form = CargarDiaViajeForm
        context = super().get_context_data(**kwargs)
        context['viaje_form'] = context['form']
        context['dia_form'] = dia_form
        dias = Viaje_Dia.objects.filter(viaje=self.get_object())
        context['dias_viaje'] = render_to_string('mostrar-dias-viaje.html', {'dias_viaje': dias})
        return context

    def post(self, request, *args, **kwargs):
        r = super().post(request, *args, **kwargs)

        viaje = self.get_object()
        viaje.estado = "ACTIVO"
        viaje.cantidadDias = viaje.viaje_dia.count()
        viaje.save()

        return r

