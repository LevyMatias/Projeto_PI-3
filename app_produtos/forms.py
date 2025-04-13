from django import forms
from . import models

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = models.Produto
        fields = ['descricao', 'quantidade', 'fornecedor', 'custo', 'valor_produto', 'lucro', 'observacao']
    