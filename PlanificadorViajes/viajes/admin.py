from django.contrib import admin
from viajes.models import Viaje_General, Viaje_Dia, Destino
# Register your models here.

class AdminViaje(admin.ModelAdmin):
    list_display = ('nombreViaje', 'cantidadDias','descripcion', 'get_usuario')
    
    def get_usuario(self, obj):
        return obj.usuario.username if obj.usuario else None
    get_usuario.short_description = 'usuario'

admin.site.register(Viaje_General, AdminViaje)

class AdminDiaViaje(admin.ModelAdmin):
    list_display = ('nombreDia', 'get_destinos')  # uso una función get_destinos para mostrar la lista en el admin
    
    def get_destinos(self, obj):
        return ", ".join([destino.nombre for destino in obj.destinos.all()])
    get_destinos.short_description = 'Destinos'  # Nombre de la columna en la lista

admin.site.register(Viaje_Dia, AdminDiaViaje)


class AdminDestino(admin.ModelAdmin):
    list_display=('nombre', 'descripcion')

    
admin.site.register(Destino, AdminDestino)
