from django import forms
from apps.pacientes.models import Paciente

class PacienteForm(forms.ModelForm):

    class Meta:

        model = Paciente

        fields = [
            'nombres',
            'apellidos',
            'tipo_documento',
            'num_documento',
            'direccion',
            'email',
            'celular',
            'referencia_nombre',
            'referencia_celular',
        ]

        labels = { 
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'tipo_documento': 'Tipo de documento',
            'num_documento': 'Número de documento',
            'direccion': 'Dirección',
            'email': 'Email',
            'celular': 'Celular',
            'referencia_nombre': 'Referencia Familiar',
            'referencia_celular': 'Celular Referencia',
        }

        widgets = {
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_documento': forms.Select(attrs={'class':'form-control'}),
            'num_documento': forms.NumberInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'referencia_nombre': forms.TextInput(attrs={'class':'form-control'}),
            'referencia_celular': forms.TextInput(attrs={'class':'form-control'}),
        }