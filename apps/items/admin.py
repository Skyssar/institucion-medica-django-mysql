from django.contrib import admin
from apps.items.models import TipoDocumento, EspecialidadMedico, Medicamentos

# Register your models here.

admin.site.register(TipoDocumento)
admin.site.register(EspecialidadMedico)
admin.site.register(Medicamentos)