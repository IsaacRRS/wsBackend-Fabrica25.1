from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name=""),

    path('registro/', views.registrar_gerente, name="registro"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

    path('pessoaBoard/', views.listar_pessoas, name="listar_pessoas"),

    path('pessoaBoard/pCriar/', views.criar_registro, name="criar_registro"),
    path('pessoaBoard/pAtualizar/<int:pk>', views.atualizar_registro, name="atualizar_registro"),
    path('pessoaBoard/pVisualizar/<int:pk>', views.visualizar_registro, name="visualizar_registro"),
    path('pessoaBoard/pDeletar/<int:pk>', views.deletar_registro, name="deletar_registro"),

    path('ipBoard/', views.listar_ips, name='listar_ips'),
    
    path('ipBoard/criarIP/', views.adicionar_ip, name='adicionar_ip'),
    path('ipBoard/atualizarIP/<int:pk>/', views.atualizar_ip, name='atualizar_ip'),
    path('ipBoard/visualizarIP/<int:pk>/', views.visualizar_ip, name='visualizar_ip'),
    path('ipBoard/deletarIP/<int:pk>/', views.deletar_ip, name='deletar_ip'),
    
]