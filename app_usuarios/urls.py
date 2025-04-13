from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    # path('cad_usuario/', views.novo_usuario, name='novo_usuario'),
]
