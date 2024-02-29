from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'quantidade', 'valor']
        widgets = {
        'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código'}),
        'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade'}),
        'valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor'}),
    }