from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def cargarDestino(request, numDia):
    return render(request, 'cargarDestino.html')


# Create your views here.
