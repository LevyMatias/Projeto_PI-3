from django.db import models

class Produto (models.Model):

    id_produto = models.AutoField(primary_key=True)
    descricao = models.TextField(max_length=100)
    quantidade = models.IntegerField()
    fornecedor = models.TextField(max_length=100)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    valor_produto = models.DecimalField(max_digits=10, decimal_places=2)
    lucro = models.DecimalField(max_digits=5, decimal_places=2)                            
    observacao = models.TextField(max_length=255)

    def __str__(self):
        return self.descricao
