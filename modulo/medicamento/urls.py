from django.urls import path
from modulo.medicamento.api import *
from modulo.medicamento.views import *

urlpatterns = [
    path('medicamento/', medicamento_api_view, name='medicamento_api'),
    path('medicamento/<int:pk>/', medicamento_detail_view, name='medicamento_detail_api' ),
    path('proovedor/', proovedor_api_view, name='proovedor_api'),
    path('proovedor/<int:pk>/', proovedor_detail_view, name='proovedor_detail_api'),
    path('estadostock/', estadoStock_api_view, name='estadostock_api'),
    path('estadostock/<int:pk>/', estadoStock_detail_view, name='estadostock_detail_api'),
    path('estadomedicamento/', estadomedicamento_api_view, name='estadomedicamento_api'),
    path('estadomedicamento/<int:pk>/', estadomedicamento_detail_view, name='estadomedicamento_detail_api'),
    path('solicitudmedicamento/', solicitudmedi_api_view, name='solicitudmedicamento_api'),
    path('solicitudmedicamento/<int:pk>/', solicitudmedi_detail_view, name='solicitudmedicamento_detail_api'),
    path('lote/', lote_api_view, name= 'lote_api'),
    path('lote/<int:pk>/', lote_detail_view, name='lote_detail_api')
    
]
