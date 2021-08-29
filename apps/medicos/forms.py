from django import forms
from apps.medicos.models import Medico, Consulta, Receta, Procedimiento

# Formulario para médico
class MedicoForm(forms.ModelForm):

    class Meta:
        model = Medico
        fields = [
            'nombres',
            'apellidos',
            'tipo_documento',
            'num_documento',
            'especialidad',
            'email',
            'celular',
        ]

        labels = { 
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'tipo_documento': 'Tipo de documento',
            'num_documento': 'Número de documento',
            'especialidad': 'Especialidad',
            'email': 'Email',
            'celular': 'Celular',
        }

        widgets = {
            'nombres': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'tipo_documento': forms.Select(),
            'num_documento': forms.NumberInput(),
            'especialidad': forms.Select(),
            'email': forms.EmailInput(),
            'celular': forms.TextInput(),
        }

# Formulario para consulta
class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = [
            'fecha',
            'paciente',
            'medico',
            'descripcion',
            'medicamentos',
            'observaciones',
        ]

        labels = { 
            'fecha': 'Fecha',
            'paciente': 'Paciente',
            'medico': 'Médico',
            'descripcion': 'Descripcion',
            'medicamentos': 'Receta',
            'observaciones': 'Observaciones',
        }

        widgets = {
            'fecha': forms.DateInput (),
            'paciente': forms.Select(),
            'medico': forms.Select(),
            'descripcion': forms.Textarea(),
            'medicamentos': forms.SelectMultiple(),
            'observaciones': forms.Textarea(),
        }

# Formulario para procedimiento
class ProcedimientoForm(forms.ModelForm):

    class Meta:
        model = Procedimiento
        fields = [
            'fecha',
            'paciente',
            'medico',
            'descripcion',
            'observaciones',
        ]

        labels = { 
            'fecha': 'Fecha',
            'paciente': 'Paciente',
            'medico': 'Médico',
            'descripcion': 'Descripcion',
            'observaciones': 'Observaciones',
        }

        widgets = {
            'fecha': forms.DateInput (),
            'paciente': forms.Select(),
            'medico': forms.Select(),
            'descripcion': forms.Textarea(),
            'observaciones': forms.Textarea(),
        }


# Formulario para receta
class RecetaForm(forms.ModelForm):

    class Meta:
        model = Receta
        fields = [
            'fecha',
            'medicamento',
            'observaciones',
        ]

        labels = { 
            'fecha': 'Fecha',
            'medicamento': 'Medicamento',
            'observaciones': 'Observaciones',
        }

        widgets = {
            'fecha': forms.DateInput (),
            'medicamento': forms.Select(),
            'observaciones': forms.Textarea(),
        }