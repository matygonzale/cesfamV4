from django.urls import path
from modulo.prescripcion.api import *
from modulo.prescripcion.views import *


urlpatterns = [
    path('prescripcion/', prescripcion_api_view, name='prescripcion_api'),
    path('prescripcion/<int:pk>/', prescripcion_detail_view, name='prescripcion_detail_api' ),
    path('reg_entregas/', entregas_api_view, name='reg_entrega_api'),
    path('reg_entregas/<int:pk>/', entregas_detail_view, name= 'reg_entrega_detail_api'),
    path('citamedica/', cita_api_view, name='citamedica_api'),
    path('citamedica/<int:pk>/', cita_detail_view, name='citamedica_detail_api'),
    path('reserva/', reserva_api_view, name='reserva_api'),
    path('reserva/<int:pk>/', reserva_detail_view, name='reserva_detail_api')
]

