from django.db.models.query import InstanceCheckMeta
from django.shortcuts import render, redirect
from apps.pacientes.forms import PacienteForm
from apps.pacientes.models import Paciente

# Create your views here.

def index(request):
    return render(request, 'pacientes/index.html')

def add_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pacientes:list_paciente')
    else:
        form = PacienteForm()

    return render(
        request,
        'pacientes/form_paciente.html',
        {'form': form}
    )

def edit_paciente(request, id_paciente):
    contexto = {}
    paciente = Paciente.objects.get(id=id_paciente)
    if request.method == 'GET':
        form = PacienteForm(instance=paciente)
    else:
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
        return redirect('pacientes:list_paciente')
    
    contexto['form'] = form
    contexto['edit'] = True
    return render(request, 'pacientes/form_paciente.html', contexto)

def list_paciente(request):
    pacientes = Paciente.objects.all().order_by('id')
    contexto = {'pacientes': pacientes}

    return render(request, 'pacientes/list_paciente.html', contexto)

def delete_paciente(request, id_paciente):
    contexto = {}
    paciente = Paciente.objects.get(id=id_paciente)
    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes:list_paciente')

    contexto['paciente'] = paciente
    return render(request, 'pacientes/delete_paciente.html', contexto)