from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .forms import CriarGerente, Login, CriarRegistro, AtualizarRegistro
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



# -----------------Registro Pessoas----------------- #



@login_required(login_url='login')
def listar_pessoas(request):

    registros = RegistroModel.objects.all()

    context = {'registros': registros}

    return render(request, 'app/pessoaBoard.html', context=context)


@login_required(login_url='login')
def criar_registro(request):

    form = CriarRegistro()

    if request.method == "POST":

        form = CriarRegistro(request.POST)

        if form.is_valid():

            form.save()

            return redirect("listar_pessoas")
        
    context = {'form': form}

    return render(request, 'app/pessoaCriar.html', context=context)

@login_required(login_url='login')
def atualizar_registro(request, pk):

    registro = RegistroModel.objects.get(id=pk)

    form = AtualizarRegistro(instance=registro)

    if request.method == 'POST':

        form = AtualizarRegistro(request.POST, instance=registro)

        if form.is_valid():

            form.save()

            return redirect("listar_pessoas")
        
    context = {'form': form}

    return render(request, 'app/pessoaAtualizar.html', context=context)

@login_required(login_url='login')
def visualizar_registro(request, pk):

    selecionar = RegistroModel.objects.get(id=pk)

    context = {'registro':selecionar}

    return render(request, 'app/pessoaVisualizar.html', context=context)

@login_required(login_url='login')
def deletar_registro(request, pk):

    registro = RegistroModel.objects.get(id=pk)

    registro.delete()

    return redirect("listar_pessoas")