from django.shortcuts import render, redirect
from registration.forms import UserRegisterForm
from django.contrib import messages

def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'La cuenta "{username}" ya fue creada. Por favor, inicia sesion.')
            return redirect('sitio-inicio')
    else:
        form = UserRegisterForm()
    return render(request, 'singup.html', {'registration_form': form})
