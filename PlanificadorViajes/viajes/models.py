from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Mes(models.Model):
    nombreMes = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreMes

class Viaje_General(models.Model):
    nombreViaje = models.CharField(max_length=250)
    cantidadDias = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=250)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    calificacion= models.IntegerField(null=True)
    mesDesde = models.ForeignKey(Mes, related_name='mes_desde', on_delete=models.SET_NULL, null=True, blank=True)
    mesHasta = models.ForeignKey(Mes, related_name='mes_hasta', on_delete=models.SET_NULL, null=True, blank=True)
    esPrivado= models.BooleanField(null = True)
    token = models.CharField(max_length=250, null=True, blank=True)
    usuariosPermitidos = models.ManyToManyField(User, related_name='viajes', blank=True)
    estado = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return  self.nombreViaje

class Viaje_Dia(models.Model):
    nombreDia = models.CharField(max_length=250)
    destinos = models.JSONField(null=True, verbose_name='estino')
    notas = models.CharField(max_length=250)
    viaje = models.ForeignKey(Viaje_General, related_name='viaje_dia', on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to="viajes", null=True)
    def __str__(self):
        return self.nombreDia
