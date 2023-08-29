from django.db import models
from django.contrib.auth.models import User

    
class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.nombre
    
class Viaje_Dia(models.Model):
    nombreDia = models.CharField(max_length=250)
    destinos= models.ManyToManyField(Destino, related_name='dias_viaje')
    notas = models.CharField(max_length=250)

    def __str__(self):
        return self.nombreDia

class Viaje_General(models.Model):
    nombreViaje = models.CharField(max_length=250)
    cantidadDias = models.IntegerField()
    descripcion = models.CharField(max_length=250)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    diasViaje= models.ManyToManyField(Viaje_Dia, related_name='viaje', null=True)


