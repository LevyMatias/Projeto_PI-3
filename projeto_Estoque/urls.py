
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_home.urls')), 
    path('produtos/', include('app_produtos.urls')), 
    path('vendas/', include('app_vendas.urls')), 
    path('usuarios/', include('app_usuarios.urls')),
    path('entradas/', include('app_entradas.urls'))
]
