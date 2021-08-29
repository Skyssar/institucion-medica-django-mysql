from django.shortcuts import render, redirect
from apps.medicos.forms import MedicoForm, ConsultaForm, ProcedimientoForm, RecetaForm
from apps.medicos.models import Medico, Consulta, Procedimiento, Receta

# Create your views here.

# Views para CRUD Medico
def add_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('medicos:list_medico')
    else:
        form = MedicoForm()

    return render(
        request,
        'medicos/medico_form.html',
        {'form': form}
    )

def edit_medico(request, id_medico):
    contexto = {}
    medico = Medico.objects.get(id=id_medico)
    if request.method == 'GET':
        form = MedicoForm(instance=medico)
    else:
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
        return redirect('medicos:edit_medico')
    
    contexto['form'] = form
    return render(request, 'medicos/medico_form.html', contexto)

def list_medico(request):
    medicos = Medico.objects.all().order_by('id')
    contexto = {'medicos': medicos}

    return render(request, 'medicos/medico_list.html', contexto)

def delete_medico(request, id_medico):
    contexto = {}
    medico = Medico.objects.get(id=id_medico)
    if request.method == 'POST':
        medico.delete()
        return redirect('medicos:list_medico')

    contexto['medico'] = medico
    return render(request, 'medicos/medico_delete.html', contexto)


# Views para CRUD Consulta
def add_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('medicos:list_consulta')
    else:
        form = ConsultaForm()

    return render(
        request,
        'consultas/consulta_form.html',
        {'form': form}
    )

def edit_consulta(request, id_consulta):
    contexto = {}
    consulta = Consulta.objects.get(id=id_consulta)
    if request.method == 'GET':
        form = ConsultaForm(instance=consulta)
    else:
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
        return redirect('medicos:list_consulta')
    
    contexto['form'] = form
    return render(request, 'consultas/consulta_form.html', contexto)

def list_consulta(request):
    consultas = Consulta.objects.all().order_by('id')
    contexto = {'consultas': consultas}

    return render(request, 'consultas/consulta_list.html', contexto)

def delete_consulta(request, id_consulta):
    contexto = {}
    consulta = Consulta.objects.get(id=id_consulta)
    if request.method == 'POST':
        consulta.delete()
        return redirect('medicos:list_consulta')

    contexto['consulta'] = consulta
    return render(request, 'medicos/consulta_delete.html', contexto)

# Views para CRUD Procedimiento
def add_procedimiento(request):
    if request.method == 'POST':
        form = ProcedimientoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('medicos:list_procedimiento')
    else:
        form = ProcedimientoForm()

    return render(
        request,
        'procedimientos/procedimiento_form.html',
        {'form': form}
    )

def edit_procedimiento(request, id_procedimiento):
    contexto = {}
    procedimiento = Procedimiento.objects.get(id=id_procedimiento)
    if request.method == 'GET':
        form = ProcedimientoForm(instance=procedimiento)
    else:
        form = ProcedimientoForm(request.POST, instance=procedimiento)
        if form.is_valid():
            form.save()
        return redirect('medicos:list_procedimiento')
    
    contexto['form'] = form
    return render(request, 'procedimientos/procedimiento_form.html', contexto)

def list_procedimiento(request):
    procedimientos = Procedimiento.objects.all().order_by('id')
    contexto = {'procedimientos': procedimientos}

    return render(request, 'procedimientos/procedimiento_list.html', contexto)

def delete_procedimiento(request, id_procedimiento):
    contexto = {}
    procedimiento = Procedimiento.objects.get(id=id_procedimiento)
    if request.method == 'POST':
        procedimiento.delete()
        return redirect('medicos:list_procedimiento')

    contexto['procedimiento'] = procedimiento
    return render(request, 'medicos/procedimiento_delete.html', contexto)