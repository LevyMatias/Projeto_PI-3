from django.db import models


class Entradas(models.Model):
    data_entrada = models.DateTimeField(verbose_name="Data de Entrada")
    produto = models.IntegerField(null=False, verbose_name="Produto")
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Custo Unitário")
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Pago")
    codigo_produto = models.IntegerField(verbose_name="Código do Produto")
    qtd_embalagem = models.IntegerField(null=False, verbose_name="Quantidade na Embalagem")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    tipo_embalagem = models.CharField(max_length=255, null=False, verbose_name="Tipo de Embalagem")
    observacoes = models.TextField(max_length=255, blank=True, verbose_name="Observações")
    fabricante = models.IntegerField(null=False, verbose_name="Fabricante")
    
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['-data_entrada']

    def __str__(self):
        return f"Entrada {self.id} - Produto: {self.produto} - Data: {self.data_entrada}"






