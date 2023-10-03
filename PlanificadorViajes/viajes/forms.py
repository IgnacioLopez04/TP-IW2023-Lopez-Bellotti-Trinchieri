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
    
    esPrivado = forms.ChoiceField(choices=[(False, 'no'),(True, 'si'),], required=False, label="¿Desea que sea privado?")

    class Meta:
        model = Viaje_General
        fields = ['nombreViaje', 'descripcion', 'mesDesde', 'mesHasta', 'esPrivado']


class CargarDiaViajeForm(forms.ModelForm):
    cargarDestino = forms.CharField(
        label="Cargar destinos",
        widget=forms.TextInput(attrs={'type': 'button', 'value': 'cargar destino', 'onclick': 'abrirMapa()'}),
        required=False,
    )

    def save(self, commit=True):
        dia_viaje = super().save(commit=False)
        dia_viaje.save() 
        return dia_viaje

    class Meta:
        model = Viaje_Dia
        fields = ['nombreDia', 'notas']

