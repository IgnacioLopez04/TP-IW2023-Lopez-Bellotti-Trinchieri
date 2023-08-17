from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    altura = models.IntegerField()