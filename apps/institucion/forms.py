from django import forms
from django.forms import widgets
from apps.institucion.models import Institucion

class InstitucionForm(forms.ModelForm):

    class Meta:

        model = Institucion

        fields = [
            'nombre',
            'direccion',
            'telefono1',
            'telefono2',
            'email',
            'icono',
        ]

        labels = { 
            'nombre': 'Nombre',
            'direccion': 'Dirección',
            'telefono1': 'Teléfono 1',
            'telefono2': 'Teléfono 2',
            'email': 'Email',
            'icono': 'Imagen',
        }

        widgets = { 
            'nombre': forms.TextInput(),
            'direccion': forms.TextInput(),
            'telefono1': forms.TextInput(),
            'telefono2': forms.TextInput(),
            'email': forms.EmailInput(),
            'icono': forms.FileInput(attrs={'accept':'image/*'}),
        }