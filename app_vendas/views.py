from django.shortcuts import redirect, render
from .models import Venda
    

def venda(request):
    obj = Venda.objects.all()
    template_name = 'vendas/vendas.html'
    context = {'obj': obj}
    return render(request, template_name, context)