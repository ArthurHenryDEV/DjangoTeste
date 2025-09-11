from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa
from .forms import PessoaForm

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