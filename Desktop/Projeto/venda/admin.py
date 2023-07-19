from django.contrib import admin
from .models import Marca, Produto

# Register your models here.
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome_marca', )

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'preco')
