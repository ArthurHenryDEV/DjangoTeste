from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Cachorro

class HelloView(View):
    def get(self, request):
        return HttpResponse('<h1>Boa Tarde</h1>')

class CachorroListView(ListView):
    model = Cachorro
    template_name = "list.html"
    context_object_name = "cachorros"
