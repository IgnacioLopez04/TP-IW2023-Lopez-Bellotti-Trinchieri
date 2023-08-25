from django import forms
from viajes.models import Viaje_General, Viaje_Dia, Imagen_Archivo

class ViajeForm(forms.ModelForm):

    class Meta:
        model = Viaje_General
        fields = ['nombreViaje', 'cantidadDias', 'fechaInicio', 'fechaFinalizacion', 'descripcion']
        widgets = {
            'fechaInicio': forms.DateInput(attrs={'type':'date'}),
            'fechaFinalizacion': forms.DateInput(attrs={'type':'date'}),
        }

class DiaViajeForm(forms.ModelForm):

    class Meta:
        model = Viaje_Dia
        fields = ['nombreDia', 'actividades', 'destinos', 'fecha', 'notas']
        widgets = {
            'fecha': forms.DateInput(attrs={'type':'date'}),
        }

class CargarImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen_Archivo
        fields = ['image']