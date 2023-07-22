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
            # 'preco': forms.FloatField(attrs={'class':'form-control'}),
            # 'img': forms.ImageField(),
            'marca': forms.TextInput(attrs={'class':'form-control'})
        }
