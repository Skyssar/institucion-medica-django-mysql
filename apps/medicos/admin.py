from django.contrib import admin
from apps.medicos.models import Medico, Receta, Consulta, Procedimiento

# Register your models here.
admin.site.register(Medico)
admin.site.register(Receta)
admin.site.register(Consulta)
admin.site.register(Procedimiento)