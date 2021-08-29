from django.urls import path

from apps.historial.views import view_historial, index

urlpatterns = [
    path('view/', view_historial, name='view_historial'),
    path('', index, name='index'),
]