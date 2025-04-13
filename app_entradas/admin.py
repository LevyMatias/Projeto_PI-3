from django.contrib import admin
from .models import Entradas

class EntradasAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'data_entrada', 'quantidade', 'valor_pago')
    list_filter = ('data_entrada', 'produto')
    search_fields = ('produto', 'observacoes')
    date_hierarchy = 'data_entrada'
    ordering = ('-data_entrada',)

admin.site.register(Entradas, EntradasAdmin)
