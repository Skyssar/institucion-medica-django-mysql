from django.shortcuts import redirect, render

from apps.institucion.models import Institucion
from apps.institucion.forms import InstitucionForm

from django.views.generic import UpdateView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    institucion = Institucion.objects.all()[:1]
    contexto = { 'institucion': institucion }
    return render(request, 'institucion/index.html', contexto)

class UpdateInfo(UpdateView):
    model = Institucion
    # form = InstitucionForm
    fields = ['nombre', 'direccion', 'telefono1', 'telefono2', 'email', 'icono']
    template_name = 'institucion/form_info.html'
    success_url = reverse_lazy('institucion:index')

def add_info(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # print(form)
        return redirect('institucion:index')
    else:
        form = InstitucionForm()  
    
    return render(
        request,
        'institucion/form_info.html',
        {'form': form}
    )

def edit_info(request, id_institucion):
    contexto = {}
    institucion = Institucion.objects.get(id=id_institucion)
    if request.method == 'GET':
        form = InstitucionForm(instance=institucion)
    else:
        form = InstitucionForm(request.POST, instance=institucion)
        if form.is_valid():
            form.save()
        return redirect('institucion:index')
    
    contexto['form'] = form
    return render(request, 'institucion/form_info.html', contexto)


def delete_info(request, id_institucion):
    contexto = {}
    institucion = Institucion.objects.get(id=id_institucion)
    if request.method == 'POST':
        institucion.delete()
        return redirect('institucion:index')

    contexto['institucion'] = institucion
    return render(request, 'institucion/delete_info.html', contexto)