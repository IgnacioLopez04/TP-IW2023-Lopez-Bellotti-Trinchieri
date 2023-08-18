from django.db import models

# Create your models here.
class Persona(models.Model):
    nombreUsuario = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    