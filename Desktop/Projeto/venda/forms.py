from django.forms import ModelForm
from django import forms
from .models import Marca, Produto

class MarcaForm(ModelForm):

    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {
            'nome_marca': forms.TextInput(attrs={'class':'form-control'})
        }

class ProdutoForm(ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome_produto': forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.TextInput(attrs={'class':'form-control'}),
            #'preco': forms.(attrs={'class':'form-control'}),
            'img': forms.FileInput(attrs={'class':'form-control'}),
            'marca': forms.Select(attrs={'class':'form-control'})
        }
