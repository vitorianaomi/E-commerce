from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length = 150)
    descricao = models.TextField(verbose_name='descrição')
    preco = models.FloatField(verbose_name='preço')
    img = models.ImageField(upload_to = 'imagens', verbose_name='imagem')
    marca = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_produto



