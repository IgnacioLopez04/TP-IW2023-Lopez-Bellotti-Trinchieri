from django.db import models
from django.contrib.auth.models import User

class Mes(models.Model):
    nombreMes = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreMes
class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)
    provincia = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.nombre

class Viaje_General(models.Model):
    nombreViaje = models.CharField(max_length=250)
    cantidadDias = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=250)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    calificacion= models.IntegerField(null=True)
    mesDesde = models.ForeignKey(Mes, related_name='mes_desde', on_delete=models.SET_NULL, null=True, blank=True)
    mesHasta = models.ForeignKey(Mes, related_name='mes_hasta', on_delete=models.SET_NULL, null=True, blank=True)
    esPrivado= models.BooleanField(null = True)

    def __str__(self):
        return  self.nombreViaje

class Viaje_Dia(models.Model):
    nombreDia = models.CharField(max_length=250)
    destinos = models.ManyToManyField(Destino, related_name='destinos')
    notas = models.CharField(max_length=250)
    viaje = models.ForeignKey(Viaje_General, related_name='viaje_dia', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nombreDia
