from django.urls import path
from . import views
from .views import listar_pessoas, criar_pessoa, deletar_pessoa, atualizar_pessoa, consultaCep
from django.http import HttpResponse

urlpatterns = [
    path('', views.home, name='home'),
    path("hello/", views.hello_view, name="hello"), # Rota para a página inicial
    path('listar/', listar_pessoas, name= 'listar_pessoas'),
    path('criar/', criar_pessoa, name= 'criar_pessoa'),
    path ('delete/<int:pk>', deletar_pessoa, name='deletar_pessoa'), 
    path('atualizar/<int:pk>', atualizar_pessoa, name='atualizar_pessoa'),
    path('consulta/', consultaCep, name='consulta_cep'),
]
