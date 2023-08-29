from django import forms
from viajes.models import Viaje_General, Viaje_Dia, Destino

class ViajeForm(forms.ModelForm):

    class Meta:
        model = Viaje_General
        fields = ['nombreViaje', 'cantidadDias', 'descripcion']

"""class DiaViajeForm(forms.ModelForm):

    class Meta:
        model = Viaje_Dia
        fields = ['nombreDia', 'destinos', 'notas']
        widgets = {
            'fecha': forms.DateInput(attrs={'type':'date'}),
        }"""

class CargarDiaViajeForm(forms.ModelForm):
    destinos = forms.ModelMultipleChoiceField(
        queryset=Destino.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

 #   nuevo_destino = forms.CharField(max_length=100, required=False, label='Nuevo Destino')
 #   acá estoy viendo como hacer para hacer un nuevo destino y ponerle cosas a hacer

    class Meta:
        model = Viaje_Dia
        fields = ['nombreDia', 'notas', 'destinos']