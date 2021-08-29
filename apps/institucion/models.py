from django.db import models
from django.db.models.base import Model

# Create your models here.

class Institucion(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono1 = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20)
    email = models.EmailField()
    icono = models.ImageField(blank=True, upload_to='uploads/')

    def __str__(self):
        return '{}'.format(self.nombre)
