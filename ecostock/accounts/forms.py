from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'quantidade', 'valor']
        widgets = {
        'codigo': forms.TextInput(attrs={'class': 'form-control','style': 'width: 400px; margin: 20px;', 'placeholder': 'Código'}),
        'nome': forms.TextInput(attrs={'class': 'form-control','style': 'width: 400px; margin: 20px;', 'placeholder': 'Nome'}),
        'quantidade': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 400px; margin: 20px;', 'placeholder': 'Quantidade'}),
        'valor': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 400px; margin: 20px;', 'placeholder': 'Valor'}),
    }