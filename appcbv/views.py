from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .forms import CachorroForm
from .models import Cachorro

class HelloView(View):
    def get(self, request):
        return HttpResponse('<h1>Boa Tarde</h1>')

class CachorroListView(ListView):
    model = Cachorro
    template_name = "list_dog.html"
    context_object_name = "cachorros"

class CachorroCreateView(CreateView):
    model = Cachorro
    form_class=CachorroForm
    template_name= "criarcachorro.html"
    success_url = reverse_lazy("listar_cachorros")
    
class CachorroUpdateView(UpdateView):
    model = Cachorro
    form_class=CachorroForm 
    template_name= "criarcachorro.html"
    context_object_name = "cachorro"
    success_url = reverse_lazy("listar_cachorros") #sucess_url(quando a url tiver sucesso) = reverse_lazy(vai redirecionar para tal link/classe/funcao).

class CachorroDeleteView(DeleteView):
    model = Cachorro
    template_name= "deletarcachorro.html"
    context_object_name = "cachorro"
    success_url = reverse_lazy("listar_cachorros")