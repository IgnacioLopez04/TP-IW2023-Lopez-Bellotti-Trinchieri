from django.db import models

class Viaje_General(models.Model):
    nombreViaje = models.CharField(max_length=250)
    cantidadDias = models.IntegerField()
    fechaInicio = models.DateField()
    fechaFinalizacion = models.DateField()
    descripcion = models.CharField(max_length=250)

    # FileField lo usamos para manejar la carga del archivo a través del formulario
    image = models.FileField(null=True)
    # El atributo image_data es un BinaryField que almacenará los datos binarios sin procesar de la imagen.
    image_data = models.BinaryField(null=True)

class Viaje_Dia(models.Model):
    nombreDia = models.CharField(max_length=250)
    actividades = models.CharField(max_length=250) #por ahora lo dejamos en un solo campo
    destinos = models.CharField(max_length=250) #por ahora lo dejamos en un solo campo
    fecha = models.DateField()
    notas = models.CharField(max_length=250)
