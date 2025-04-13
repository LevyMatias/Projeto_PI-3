from django import forms
from .models import Entradas

class EntradasForm(forms.ModelForm):
    class Meta:
        model = Entradas
        fields = '__all__'
        widgets = {
            'data_entrada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
        
    def clean_valor_pago(self):
        valor_pago = self.cleaned_data.get('valor_pago')
        if valor_pago and valor_pago <= 0:
            raise forms.ValidationError("O valor pago deve ser maior que zero.")
        return valor_pago
        
    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade and quantidade <= 0:
            raise forms.ValidationError("A quantidade deve ser maior que zero.")
        return quantidade 