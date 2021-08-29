from django.shortcuts import render, redirect
from apps.pacientes.models import Paciente
from apps.medicos.models import Consulta, Procedimiento, Medicamentos
from apps.items.models import TipoDocumento

# Create your views here.

def index(request):
    return render(request, 'historial/index.html')


# def view_historial(request, cedula_paciente):
#     paciente = Paciente.objects.get(num_documento=cedula_paciente)
#     contexto = {}
#     if paciente:
#         consultas = Consulta.objects.filter(paciente__num_documento=cedula_paciente)
#         procedimientos = Procedimiento.objects.filter(paciente__num_documento=cedula_paciente)

#         contexto ['consultas'] = consultas
#         contexto['procedimientos'] = procedimientos
    
#     contexto['paciente'] = paciente
    
#     return render(request, 'historial/historial_view.html', contexto)

def view_historial(request):
    tipos_documento = TipoDocumento.objects.all()

    contexto = {}
    contexto['tipos_documento'] = tipos_documento

    if request.method == 'POST':
        busqueda_num = request.POST['numDocumento']
        busqueda_tipo = request.POST['tipoDocumento']
        paciente = Paciente.objects.filter(num_documento=busqueda_num).filter(tipo_documento__id=busqueda_tipo)
        
        contexto['busqueda'] = {'tipo_documento': busqueda_tipo, 'num_documento': busqueda_num }
        contexto['encontrado'] = False

        if paciente:
            consultas = Consulta.objects.filter(paciente__num_documento=busqueda_num)
            procedimientos = Procedimiento.objects.filter(paciente__num_documento=busqueda_num)

            contexto['encontrado'] = True
            contexto ['consultas'] = consultas
            contexto['procedimientos'] = procedimientos
        
        contexto['paciente'] = paciente

    return render(request, 'historial/historial_view.html', contexto)