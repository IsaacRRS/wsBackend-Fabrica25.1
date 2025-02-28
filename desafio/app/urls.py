from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name=""),

    path('registro/', views.registrar_gerente, name="registro"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]