from django.contrib import admin
from viajes.models import Viaje_General, Viaje_Dia
# Register your models here.

class AdminViaje(admin.ModelAdmin):
    list_display = ('nombreViaje', 'cantidadDias','descripcion')

admin.site.register(Viaje_General, AdminViaje)

class AdminDiaViaje(admin.ModelAdmin):
    list_display = ('nombreDia', 'get_destinos')  # Aquí estamos usando una función get_destinos
    
    def get_destinos(self, obj):
        return ", ".join([destino.nombre for destino in obj.destinos.all()])
    get_destinos.short_description = 'Destinos'  # Nombre de la columna en la lista

admin.site.register(Viaje_Dia, AdminDiaViaje)
