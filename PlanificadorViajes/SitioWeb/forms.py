from django import forms
from django.core.exceptions import ValidationError
from SitioWeb.models import Persona

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombreUsuario', 'email', 'password']

