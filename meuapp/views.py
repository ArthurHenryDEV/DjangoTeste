from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa
from .forms import PessoaForm
import requests

def home(request):
    return render(request, 'home.html')

# Create your views here.

def hello_view(request): 
    return HttpResponse("Hello World")

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'list.html', {'pessoas': pessoas})

def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'create.html', {'pessoa': form})

def deletar_pessoa(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect ('listar_pessoas')
    return render(request, 'confirmar_delete.html', {'pessoa': pessoa}) 

def atualizar_pessoa(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'create.html', {'pessoa': form})


#  Config API
def consultaCep(request):
    response = requests.get("https://viacep.com.br/ws/58046518/json/", verify=False)
    dadosEndereco = response.json()
    endereco = Pessoa.objects.create(
        nome= dadosEndereco["logradouro"], #GAMBIARRA(!!!!)
        idade = dadosEndereco["ibge"], #GAMBIARRA(!!!!)
        email = "sivirino@gmail.com" #GAMBIARRA(!!!!)
    )
    return HttpResponse(dadosEndereco("logradouro"))