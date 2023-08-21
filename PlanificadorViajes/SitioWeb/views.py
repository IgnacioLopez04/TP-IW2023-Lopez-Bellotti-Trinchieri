from django.shortcuts import render, redirect

from SitioWeb.models import Persona
from SitioWeb.forms import UserRegisterForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html', {})

@login_required
def cargarViaje(request):
    return render(request, 'viaje.html', {})

#def login(request):
#    form = FormPersona()
#    return render(request, 'registration/login.html', {'form_login': form})

def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'La cuenta ya fue creada. Por favor, inicia sesion.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/singup.html', {'registration_form': form})