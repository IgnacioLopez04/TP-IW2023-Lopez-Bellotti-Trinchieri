from django.shortcuts import render, redirect

from SitioWeb.forms import UserRegisterForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'inicio.html', {})

@login_required
def cargarViaje(request):
    return render(request, 'viaje.html', {})

def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'La cuenta {username} ya fue creada. Por favor, inicia sesion.')
            return redirect('sitio-inicio')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/singup.html', {'registration_form': form})