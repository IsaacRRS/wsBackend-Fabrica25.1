from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from .models import RegistroModel, IPModel

import requests



def index(request):

    return render(request, 'app/index.html')



def registrar_gerente(request):

    form = CriarGerente()

    if request.method == "POST":

        form = CriarGerente(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")
        
    context = {'form':form}

    return render(request, 'app/gerenteRegistro.html', context=context)

def login(request):

    form = Login()

    if request.method == "POST":

        form = Login(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            usuario = authenticate(request, username=username, password=password)

            if usuario is not None:

                auth.login(request, usuario)

                return redirect("listar_pessoas")         

    context = {'form':form}

    return render(request, 'app/gerenteLogin.html', context=context)


def logout(request):

    auth.logout(request)

    return redirect("login")

