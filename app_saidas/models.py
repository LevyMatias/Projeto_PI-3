from django.db import models

class Saida(models.Model):
    codigo_saida = models.AutoField(primary_key=True), 
    data_saida = models.DateField(auto_now_add=True), 
    produto = models.IntegerField(null=False), 
    quantidade = models.IntegerField(null=False), 
    custo = models.DecimalField(max_digits=10, decimal_places=2, null=False), 
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, null=False), 
    lucro_porcentagem = models.DecimalField(max_digits=4, decimal_places=2), 
    lucro = models.DecimalField(max_digits=10, decimal_places=2, null=False)
