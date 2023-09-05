from django.contrib import admin
from viajes.models import Viaje_General, Viaje_Dia, Destino, Mes
# Register your models here.

class AdminViaje(admin.ModelAdmin):
    list_display = ('nombreViaje', 'cantidadDias','descripcion', 'get_usuario','calificacion', 'get_mesDesde', 'get_mesHasta')
    
    def get_usuario(self, obj):
        return obj.usuario.username if obj.usuario else None
    get_usuario.short_description = 'usuario'

    def get_mesDesde(self, obj):
        return obj.mesDesde.nombreMes if obj.mesDesde else None
    get_mesDesde.short_description = 'mesDesde'

    def get_mesHasta(self, obj):
        return obj.mesHasta.nombreMes if obj.mesHasta else None
    get_mesHasta.short_description = 'mesHasta'

admin.site.register(Viaje_General, AdminViaje)

class AdminDiaViaje(admin.ModelAdmin):
    list_display = ('nombreDia', 'viaje','get_destinos','notas')  # uso una función get_destinos para mostrar la lista en el admin
    
    def get_destinos(self, obj):
        return ", ".join([destino.nombre for destino in obj.destinos.all()])
    get_destinos.short_description = 'Destinos'  # Nombre de la columna en la lista

admin.site.register(Viaje_Dia, AdminDiaViaje)


class AdminDestino(admin.ModelAdmin):
    list_display=('nombre', 'descripcion')
    
admin.site.register(Destino, AdminDestino)

class AdminMeses(admin.ModelAdmin):
    list_display=('nombreMes',)
    
admin.site.register(Mes, AdminMeses)