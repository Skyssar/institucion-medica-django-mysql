from django.db import models
from apps.items.models import TipoDocumento

# Create your models here.

class Paciente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    
    num_documento = models.BigIntegerField()
    direccion = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    celular = models.CharField(max_length=10)
    referencia_nombre = models.CharField(max_length=50)
    referencia_celular = models.CharField(max_length=10)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)
