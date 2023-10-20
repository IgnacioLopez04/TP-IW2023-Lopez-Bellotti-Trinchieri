from django import forms
from viajes.models import Viaje_General, Viaje_Dia, Mes, imagen
from django import forms
from django.forms import modelformset_factory


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
    
    esPrivado = forms.ChoiceField(choices=[(False, 'No'),(True, 'Si'),], required=False, label="¿Desea que sea privado?")

    class Meta:
        model = Viaje_General
        fields = ['nombreViaje', 'descripcion', 'mesDesde', 'mesHasta', 'esPrivado']


class CargarDiaViajeForm(forms.ModelForm):
    cargarDestino = forms.CharField(
        label="Cargar destinos",
        widget=forms.TextInput(attrs={'type': 'button', 'value': 'Cargar destino', 'onclick': 'abrirMapa()'}),
        required=False,
    )

    def save(self, commit=True):
        dia_viaje = super().save(commit=False)
        dia_viaje.save()
        return dia_viaje

    class Meta:
        model = Viaje_Dia
        fields = ['nombreDia', 'notas']


class ImagenForm(forms.ModelForm):
    imagen = forms.ImageField(label="Cargar Imagen", required=False)

    class Meta:
        model = imagen
        fields = ['imagen']

ImagenFormSet = modelformset_factory(imagen, fields=['imagen'], extra=2, max_num=5)  # Puedes ajustar `extra` y `max_num` según tus necesidades
