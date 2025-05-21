from django.shortcuts import render, redirect
from .models import Produto
from . import forms

def cad_produtos(request):
    form = forms.ProdutoForm()
    if request.method == 'POST':
        form = forms.ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:lista_produtos')
    template_name = 'produtos/cadprodutos.html'
    context = {'form': form}
    return render(request, template_name, context)
    

def produto(request):
    obj = Produto.objects.all()
    template_name = 'produtos/produtos.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def deletar_produto(request, id_produto):
    obj = Produto.objects.get(id_produto=id_produto)
    obj.delete()
    return redirect('produtos:lista_produtos')

# # grafico
# def grafico(request):
#     labels = []
#     data = []
    
#     queryset = Produto.objects.order_by('-quantidade')[:10]
#     for produto in queryset:
#         labels.append(produto.descricao)
#         data.append(produto.quantidade)
#     return render(request, 'Arquivos_HTML/graficos.html', {'labels': labels, 'data': data,})
