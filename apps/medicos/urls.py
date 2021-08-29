from django.urls import path

from apps.medicos.views import add_medico, list_medico, delete_medico, edit_medico
from apps.medicos.views import add_consulta, list_consulta, delete_consulta, edit_consulta
from apps.medicos.views import add_procedimiento, list_procedimiento, delete_procedimiento, edit_procedimiento

urlpatterns = [
    path('add/', add_medico, name='add_medico'),
    path('list/', list_medico, name='list_medico'),
    path('edit/<int:id_medico>', edit_medico, name='edit_medico'),
    path('delete/<int:id_medico>', delete_medico, name='delete_medico'),

    path('consultas/add/', add_consulta, name='add_consulta'),
    path('consultas/list/', list_consulta, name='list_consulta'),
    path('consultas/edit/<int:id_consulta>', edit_consulta, name='edit_consulta'),
    path('delete/<int:id_>', delete_consulta, name='delete_consulta'),

    path('procedimientos/add/', add_procedimiento, name='add_procedimiento'),
    path('procedimientos/list/', list_procedimiento, name='list_procedimiento'),
    path('procedimientos/edit/<int:id_procedimiento>', edit_procedimiento, name='edit_procedimiento'),
    path('delete/<int:id_>', delete_procedimiento, name='delete_procedimiento'),
]