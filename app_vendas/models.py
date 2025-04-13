from django.db import models

class Venda(models.Model):
    código_venda = models.AutoField(primary_key=True)
    código_produto = models.IntegerField()
    produto = models.TextField(max_length=255, null=False)
    data_venda = models.DateTimeField(auto_now=True, null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantidade_venda = models.IntegerField(default=0, null=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False)
    total_geral = models.IntegerField(null=False)
    forma_pagamento = models.TextField(max_length=255, null=False)
    observacoes = models.TextField(max_length=255)   
