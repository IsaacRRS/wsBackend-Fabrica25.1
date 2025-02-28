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

]