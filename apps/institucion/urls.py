from django.urls import path

from apps.institucion.views import index, add_info, edit_info, delete_info
from apps.institucion.views import UpdateInfo

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_info, name='add_info'),
    # path('edit/<int:id_institucion>/', edit_info, name='edit_info'),
    path('delete/<int:id_institucion>/', delete_info, name='delete_info'),

    path('edit/<pk>/', UpdateInfo.as_view(), name='edit_info'),
]

