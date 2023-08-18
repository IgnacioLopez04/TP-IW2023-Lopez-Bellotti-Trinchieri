from django.contrib import admin
from SitioWeb.models import Persona
# Register your models here.

class AdminPersona(admin.ModelAdmin):
    list_display = ('nombreUsuario', 'email',)

admin.site.register(Persona, AdminPersona)