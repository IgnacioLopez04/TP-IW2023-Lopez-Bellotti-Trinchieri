from django import forms
from viajes.models import Viaje_General, Viaje_Dia, Mes
from django import forms


class ViajeForm(forms.ModelForm):
    nombreViaje= forms.CharField(label= "Nombre del viaje")
    descripcion= forms.CharField(label= "Descripcion")
    
    mesDesde = forms.ModelChoiceField(
        queryset=Mes.objects.all(),
        empty_label="Mes inicial", 
        label="¿A partir de qué mes recomiendas realizarlo?"
    )
    mesHasta = forms.ModelChoiceField(
        queryset=Mes.objects.all(),
        empty_label="Mes final",  
        label="¿Hasta cuándo?"
    )
    
    esPrivado = forms.ChoiceField(choices=[(False, 'No'),(True, 'Si'),], required=False, label="¿Desea que sea privado?")

    class Meta:
        model = Viaje_General
        fields = ['nombreViaje', 'descripcion', 'mesDesde', 'mesHasta', 'esPrivado']


class CargarDiaViajeForm(forms.ModelForm):
    cargarDestino = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'type': 'button', 'value': 'Cargar ubicaciones', 'onclick': 'abrirMapa()'}),
        required=False,
    )


    def save(self, commit=True):
        dia_viaje = super().save(commit=False)
        dia_viaje.save()
        return dia_viaje

    class Meta:
        model = Viaje_Dia
        fields = ['nombreDia', 'notas', 'imagen']
        labels = {
            'nombreDia': 'Nombre del dia',
            'notas': 'Notas',
        }

    imagen = forms.ImageField(required=False, label= '¿Deseas cargar una foto del dia?')


