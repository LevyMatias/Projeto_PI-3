from django.urls import path
from . import views

app_name = 'vendas'

urlpatterns = [
    path('', views.venda, name='lista_vendas'),
]
