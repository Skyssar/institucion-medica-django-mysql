from django.urls import path

from apps.pacientes.views import index, add_paciente, edit_paciente, list_paciente, delete_paciente

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_paciente, name='add_paciente'),
    path('list/', list_paciente, name='list_paciente'),
    path('edit/<int:id_paciente>', edit_paciente, name='edit_paciente'),
    path('delete/<int:id_paciente>', delete_paciente, name='delete_paciente'),
]
