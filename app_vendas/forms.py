from django import forms
from . import models

class VendaForm(forms.ModelForm):
    class Meta:
        model = models.Venda
        fields = ['código_produto', 'produto', 'preco', 'quantidade_venda', 'total','total_geral', 'forma_pagamento' ,'observacoes']