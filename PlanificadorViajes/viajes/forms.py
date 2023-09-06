from django import forms
from viajes.models import Viaje_General, Viaje_Dia, Destino, Mes



class ViajeForm(forms.ModelForm):
    nombreViaje= forms.CharField(label= "Nombre del viaje")
    descripcion= forms.CharField(label= "Descripcion")
    mesDesde = forms.ModelChoiceField(
        queryset=Mes.objects.all(),
        empty_label="Mes inicial", 
        label="¿A partir del qué mes recomiendas realizarlo?"
    )
    mesHasta = forms.ModelChoiceField(
        queryset=Mes.objects.all(),
        empty_label="Mes final",  
        label="¿Y hasta cuándo?"
    )
    class Meta:
        model = Viaje_General
        fields = ['nombreViaje', 'descripcion', 'mesDesde', 'mesHasta']


class CargarDiaViajeForm(forms.ModelForm):
   #carga la lista con los destinos que existen
    destinos = forms.ModelChoiceField(   
        queryset=Destino.objects.all(),
        widget=forms.Select,
        required=False,
        empty_label="Seleccione un destino o ingrese uno nuevo"
    )

    def save(self, commit=True):
        dia_viaje = super().save(commit=False)
        dia_viaje.save() 
        return dia_viaje

    class Meta:
        model = Viaje_Dia
        fields = ['nombreDia', 'notas', 'destinos']

