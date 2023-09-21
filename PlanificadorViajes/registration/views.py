from django.shortcuts import render, redirect
from registration.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Imports para el envio del mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model
from .token import account_activation_token

from .forms import User
from viajes.models import Viaje_General

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        
        messages.success(request, f'Gracias por confirmar tu correo electronico. Ahora puede iniciar sesion con tu nueva cuenta.')
        return redirect('login')
    else:
        messages.error(request, f'Link de validacion es invalido!')
    
    return redirect('sitio-inicio')

def activateEmail(request, user, to_email):
    mail_subject = 'Activa tu cuenta de usuario en Los Tres Viajeros.'
    messages_content = render_to_string('template_mail.html',{
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http' 
    })
    email = EmailMessage(mail_subject, messages_content, to=[to_email])
    if email.send():
        messages.success(request, f'Por favor "{user}", dirigite a tu casilla de correo "{to_email}" y presiona sobre el link de activacion \
            para validar su correo electrónico.')
    else:
        messages.error(request, f'Hubo un problema al enviar el email a {to_email}. Vuelva a intentarlo más tarde.')


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email = email).exists():
                messages.error(request, f'Este email ya existe. Por favor ingresa uno nuevo.')
                return render(request, 'signup.html', {'registration_form': form})
            
            user = form.save(commit=False) #no se guarda en la bd
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('sitio-inicio')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'registration_form': form})

@login_required
def user(request):
    email = request.user.email
    user_name = request.user.username
    user = User.objects.get(username=user_name)
    
    viajes = Viaje_General.objects.filter(usuario=user.pk).count()
    
    info = {
        'email': email,
        'user': user,
        'viajes': viajes,
    }
    
    return render(request, 'user.html', {'info': info})
