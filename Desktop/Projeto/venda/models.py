from django.db import models

# Create your models here.
class Marca(models.Model):
    nome_marca = models.CharField(max_length = 150)

    def __str__(self):
        return self.nome_marca

class Produto(models.Model):
    nome_produto = models.CharField(max_length = 150)
    descricao = models.TextField()
    preco = models.FloatField()
    img = models.ImageField(upload_to = 'imagens')
    marca = models.ForeignKey(Marca, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome_produto



