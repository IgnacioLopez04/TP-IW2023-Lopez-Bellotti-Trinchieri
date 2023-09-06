from django import forms
from viajes.models import Viaje_General, Viaje_Dia, Destino, Mes



class ViajeForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     meses_dict = kwargs.pop('meses_dict', None)  # Extrae el diccionario si se proporciona
    #     super(ViajeForm, self).__init__(*args, **kwargs)
        
    #     if meses_dict:
    #             # Personaliza las opciones del campo 'mesDesde' utilizando el diccionario
    #             self.fields['mesDesde'].choices = [(v, k) for k, v in meses_dict.items()]

    #             # Personaliza las opciones del campo 'mesHasta' utilizando el diccionario
    #             self.fields['mesHasta'].choices = [(v, k) for k, v in meses_dict.items()]
    
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

