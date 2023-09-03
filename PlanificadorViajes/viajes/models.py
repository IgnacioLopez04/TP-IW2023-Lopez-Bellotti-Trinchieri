from django.db import models
from django.contrib.auth.models import User


class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.nombre

class Viaje_General(models.Model):
    nombreViaje = models.CharField(max_length=250)
    cantidadDias = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=250)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return  self.nombreViaje

class Viaje_Dia(models.Model):
    nombreDia = models.CharField(max_length=250)
    destinos = models.ManyToManyField(Destino, related_name='destinos')
    notas = models.CharField(max_length=250)
    viaje = models.ForeignKey(Viaje_General, related_name='viaje_dia', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombreDia

class Viaje_Dia_Destino(models.Model):
    dia_viaje = models.ForeignKey(
        Viaje_Dia, on_delete=models.CASCADE
    )
    destino = models.ForeignKey(
        Destino, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.destino.nombre