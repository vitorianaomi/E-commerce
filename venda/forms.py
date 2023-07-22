from django.forms import ModelForm
from django import forms
from .models import Produto

class ProdutoForm(ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome_produto': forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.TextInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'})
        }
