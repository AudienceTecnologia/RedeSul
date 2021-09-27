from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('consorcio_cadastro/<str:tipo_venda>/<str:tipo_pessoa>', views.consorcio_cadastro, name='consorcio_cadastro'),
    path('consorcio_relatorio/', views.consorcio_relatorio, name='consorcio_relatorio'),

    path('administradora_lista/', views.administradora_lista, name='administradora_lista'),

    path('representante_lista/', views.representante_lista, name='representante_lista'),
]