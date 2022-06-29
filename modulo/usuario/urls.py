from unicodedata import name
from django.urls import path
from modulo.usuario.api import *
from modulo.usuario.views import *


urlpatterns = [
    path('paciente/', paciente_api_view, name='paciente_api' ),
    path('paciente/<int:pk>/', paciente_detail_view, name='paciente_detial_api'),
    path('doctor/', doctor_api_view, name= 'doctor_api'),
    path('doctor/<int:pk>/', doctor_detail_view, name= 'doctor_detail_api'),
    path('farmaceuta/', farmaceuta_api_view, name= 'farmaceuta_api'),
    path('farmaceuta/<int:pk>/', farmaceuta_detail_view, name='farmaceuta_detail_api'),
    path('carnet/', carnet_api_view, name= 'carnet_api'),
    path('carnet/<int:pk>/', carnet_detail_view, name='carnet_detail_api'),
    path('user/', user_api_view, name= 'user_api'),
    path('user/<str:pk>/', user_detail_view, name= 'user_detail_api'),
    path('index/', index, name= 'index'),
    path('crearpaciente/', crear_paciente, name= 'crearpaciente'),
    path('editarpaciente/<int:pk>/', editar_paciente, name= 'editarpaciente')
]
