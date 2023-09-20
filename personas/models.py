from django.db import models

# Create your models here.
#Clase personas
class Persona(models.Model):
    nombre = models.CharField(max_length=30,blank=False)
    apellido = models.CharField(max_length=30,blank=False)
    cedula = models.CharField(max_length=20,blank=False)
    direccion = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
