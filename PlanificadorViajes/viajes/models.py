from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    actividades = models.TextField()
    
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
    diasViaje= models.ManyToManyField(Viaje_Dia, related_name='viaje')


