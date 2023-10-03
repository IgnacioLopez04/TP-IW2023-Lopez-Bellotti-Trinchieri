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
from registration.token import account_activation_token
from django.contrib import messages
import json
from django.http import JsonResponse

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
            viaje_form.token = account_activation_token.make_token(viaje_form.usuario)
            # data = json.loads(request.body)
            # correos = data.get('correos', None)
            # if es_privado and correos:

            enviar_correos_privados(request,correos,viaje_form.token)
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
    
    if request.user == viaje.usuario:
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

def aceptar_solicitud(request, tk):
    try:
        viaje = get_object_or_404(Viaje_General, token = tk)
    except:
        viaje = None
    if viaje is not None and account_activation_token(viaje, tk):
        return redirect('detalle-viaje-token')
    return redirect('usuario')

def enviar_correos_privados(request, to_email, token):
    
    # mail_subject = 'Invitacion a un viaje privado en Los Tres Viajeros'
    # messages_content = render_to_string('invitacion_mail.html',{
    #     'domain': get_current_site(request).domain,
    #     'token': token,
    #     'protocol': 'https' if request.is_secure() else 'http'
    # }) 
    
    # # Convertir la lista de correos en una lista separada por comas
    # destinatarios = to_email.split(',')

    # # Enviar el correo a cada destinatario
    # for destinatario in destinatarios:
    #     email = EmailMessage(mail_subject, messages_content, to=[destinatario])
    #     if email.send():
    #         messages.success(request, f'La invitacion fue enviada.')
    #     else:
    #         messages.error(request, f'No envie el mail')
    # Configurar los datos del servidor SMTP y el correo remitente
    smtp_server = "{{ EMAIL_HOST }}"
    smtp_port = "{{EMAIL_PORT}}"
    remitente = "{{EMAIL_FROM}}"
    password = "{{EMAIL_HOST_PASSWORD}}"

    # Crear el mensaje de correo
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['Subject'] = 'Invitación a un viaje privado en Los Tres Viajeros'

    # Cuerpo del mensaje
    mensaje.attach(MIMEText('¡Te invitamos a nuestro viaje privado!', 'plain'))

    # Convertir la lista de correos en una lista separada por comas
    destinatarios = to_email.split(',')

    # Enviar el correo a cada destinatario
    for destinatario in destinatarios:
        mensaje['To'] = destinatario
        try:
            # Iniciar una conexión SMTP y enviar el correo
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(remitente, password)
            server.sendmail(remitente, destinatario, mensaje.as_string())
            server.quit()
        except Exception as e:
            # Manejar errores de envío de correo
            print(f"Error al enviar correo a {destinatario}: {str(e)}")
