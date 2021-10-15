from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('consorcio_cadastro/<str:tipo_venda>/<str:tipo_pessoa>', views.consorcio_cadastro, name='consorcio_cadastro'),
    path('consorcio_relatorio/', views.consorcio_relatorio, name='consorcio_relatorio'),

    path('administradora_lista/', views.administradora_lista, name='administradora_lista'),
    path('administradora_delete/<int:id>', views.administradora_delete, name='administradora_delete'),
    path('administradora_edit/<int:administradora_id>/<int:comissionamento_id>', views.administradora_edit, name='administradora_edit'),
    path('administradora_nova_regra/<int:administradora_id>/<int:comissionamento_id>', views.administradora_nova_regra, name='administradora_nova_regra'),

    path('representante_lista/', views.representante_lista, name='representante_lista'),
    path('representante_delete/<int:id>', views.representante_delete, name='representante_delete'),
    path('representante_edit/<int:id>', views.representante_edit, name='representante_edit'),

    path('financiamento_cadastro/<str:tipo_venda>/<str:tipo_pessoa>', views.financiamento_cadastro, name='financiamento_cadastro'),
    path('financiamento_relatorio/', views.financiamento_relatorio, name='financiamento_relatorio'),

    path('homeequity_cadastro/<str:tipo_venda>/<str:tipo_pessoa>', views.homeequity_cadastro, name='homeequity_cadastro'),
    path('homeequity_relatorio/', views.homeequity_relatorio, name='homeequity_relatorio'),

    path('user_edit_name/<int:id>', views.user_edit_name, name='user_edit_name'),
    path('change_password/', views.change_password, name='change_password'),
    path('user_lista/', views.user_lista, name='user_lista'),
    path('user_delete/<int:id>', views.user_delete, name='user_delete'),
    path('user_edit/<int:id>', views.user_edit, name='user_edit'),
    
    path('comissao_pagar/', views.comissao_pagar, name='comissao_pagar'),
    path('comissao_receber/', views.comissao_receber, name='comissao_receber'),
    path('fluxos_futuros/', views.fluxos_futuros, name='fluxos_futuros'),
    path('financeiro_recebidas/', views.financeiro_recebidas, name='financeiro_recebidas'),
    path('financeiro_pagas/', views.financeiro_pagas, name='financeiro_pagas'),
    
    path('lances_relatorio/', views.lances_relatorio, name='lances_relatorio'),
]