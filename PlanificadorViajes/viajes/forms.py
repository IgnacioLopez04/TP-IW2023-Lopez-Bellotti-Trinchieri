from django import forms
from viajes.models import Viaje_General, Viaje_Dia, Destino

class ViajeForm(forms.ModelForm):
    #le doy un formato y label diferente a los campos
    cantidadDias = forms.IntegerField(min_value=0, max_value= 90, label="Cantidad de dias")
    nombreViaje= forms.CharField(label= "Nombre del viaje")
    descripcion= forms.CharField(label= "Descripcion")
    class Meta:
        model = Viaje_General
        fields = ['nombreViaje', 'cantidadDias', 'descripcion']


class CargarDiaViajeForm(forms.ModelForm):
   #carga la lista con los destinos que existen
    destinos = forms.ModelChoiceField(
        queryset=Destino.objects.all(),
        widget=forms.Select,
        required=False,
        empty_label="Seleccione un destino o ingrese uno nuevo"
    )

    nuevo_destino = forms.CharField(max_length=100, required=False, label='Nuevo Destino')

    def save(self, commit=True):
        dia_viaje = super().save(commit=False)

        nuevo_destino = self.cleaned_data.get('nuevo_destino')
        if nuevo_destino:
            destino_nuevo, created = Destino.objects.get_or_create(nombre=nuevo_destino)
            dia_viaje.destinos.add(destino_nuevo)

        if commit:
            dia_viaje.save()
        return dia_viaje

    class Meta:
        model = Viaje_Dia
        fields = ['nombreDia', 'notas', 'destinos']

#form viejo de diaviaje
"""class DiaViajeForm(forms.ModelForm):

    class Meta:
        model = Viaje_Dia
        fields = ['nombreDia', 'destinos', 'notas']
        widgets = {
            'fecha': forms.DateInput(attrs={'type':'date'}),
        }"""