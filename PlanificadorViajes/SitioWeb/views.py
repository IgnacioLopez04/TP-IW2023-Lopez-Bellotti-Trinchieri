from django.shortcuts import render, redirect

from SitioWeb.models import Persona
#from SitioWeb.forms import FormPersona

from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html', {})

# def persona_Carga(request): (esto es lo que vimos en clase, deberiamos implementarlo)
    if request.method == "POST":
        form = FormPersona(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/inicio/")
    else:
        form = FormPersona()

    return render(request, 'inicio.html', {'form_Persona': form})