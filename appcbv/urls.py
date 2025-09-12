from django.urls import path

from .views import HelloView, CachorroListView, CachorroCreateView, CachorroUpdateView, CachorroDeleteView

urlpatterns = [
    path("",HelloView.as_view(), name= 'index'),
    path("listar/", CachorroListView.as_view(), name="listar_cachorros"),
    path("criar/", CachorroCreateView.as_view(), name="criar_cachorro"),
    path("atualizar/<int:pk>", CachorroUpdateView.as_view(), name="atualizar_cachorro"),
    path("deletar/<int:pk>", CachorroDeleteView.as_view(), name='deletar_cachorro'),
    ]