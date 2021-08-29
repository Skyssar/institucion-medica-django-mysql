from django.db import models

# Create your models here.

class TipoDocumento(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.tipo)

class EspecialidadMedico(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Medicamentos(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.tipo)