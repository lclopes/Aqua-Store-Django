from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class CategoriaAguas(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        db_table = 'categoria_aguas'

    def get_absolute_path(self):
        return reverse('aquastore_app:lista_aguas_por_categoria', args=[self.slug])

    def __str__(self):
        return self.nome


class Agua(models.Model):
    categoria = models.ForeignKey(CategoriaAguas, related_name='aguas', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=200, db_index=True)
    imagem = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)

    class Meta:
        db_table = 'agua'

    def get_absolute_path(self):
        return reverse('aquastore_app:exibe_agua', args=[self.id])

    def __str__(self):
        return self.nome

    def atualiza(self):
        return reverse('aquastore_app:atualiza',args=[self.id])

    def deleta(self):
        return reverse('aquastore_app:deleta',args=[self.id])


class Carrinho(models.Model):
    aguas = models.ForeignKey(Agua, related_name='aguas', on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    qtd = models.PositiveIntegerField()

    def preco_total(self):
        return self.preco * self.qtd

