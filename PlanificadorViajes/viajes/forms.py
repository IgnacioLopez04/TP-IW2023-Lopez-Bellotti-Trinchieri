from django import forms
from viajes.models import Viaje_General, Viaje_Dia, Destino, Viaje_Dia_Destino

class ViajeForm(forms.ModelForm):
    #le doy un formato y label diferente a los campos
    nombreViaje= forms.CharField(label= "Nombre del viaje")
    descripcion= forms.CharField(label= "Descripcion")
    class Meta:
        model = Viaje_General
        fields = ['nombreViaje', 'descripcion']


class CargarDiaViajeForm(forms.ModelForm):
   #carga la lista con los destinos que existen
    destinos = forms.ModelChoiceField(   
        queryset=Destino.objects.all(),
        widget=forms.Select,
        required=False,
        empty_label="Seleccione un destino"
    )

    nuevo_destino = forms.CharField(max_length=100, required=False, label='Otro Destino')

    def save(self, commit=True):
        dia_viaje = super().save(commit=False)

        nuevo_destino = self.cleaned_data.get('nuevo_destino')
        if nuevo_destino:
            destino_nuevo, created = Destino.objects.get_or_create(nombre=nuevo_destino)
            dia_viaje.save() #Primero se guarda la instancia para despues agregar el destino m2m
            dia_viaje.destinos.add(destino_nuevo)

        return dia_viaje

    class Meta:
        model = Viaje_Dia
        fields = ['nombreDia', 'notas', 'destinos']