from django.db import models
from apps.items.models import Medicamentos, EspecialidadMedico, TipoDocumento
from apps.pacientes.models import Paciente

# Create your models here.

class Medico(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    num_documento = models.BigIntegerField()
    especialidad = models.ForeignKey(EspecialidadMedico, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    celular = models.BigIntegerField()

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)

class Receta(models.Model):
    fecha = models.DateField()
    medicamento = models.ForeignKey(Medicamentos, null=True, blank=True, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return '{} - {}'.format(self.fecha, self.medicamento)

class Consulta(models.Model):
    fecha = models.DateField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    descripcion = models.TextField()
    medicamentos = models.ManyToManyField(Receta, blank=True)
    observaciones = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return '{} - {}'.format(self.fecha, self.paciente)

class Procedimiento(models.Model):
    fecha = models.DateField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    descripcion = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return '{} - {}'.format(self.fecha, self.paciente)
