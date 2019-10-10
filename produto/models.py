from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        db_table='categoria'

    def get_absolute_path(self):
        return reverse('produto:lista_produtos_por_categoria', args=[self.slug])

    def __str__(self):
        return self.nome


# A view abaixo é utilizada para listar os produtos de uma determinada categoria
# Este URLconf trata requisições para http://localhost:8000/computador/
# path('<slug:slug_da_categoria>/', views.lista_produtos, name='lista_produtos_por_categoria'),
# /computador/
# /celular/
# /eletrodomestico/

# from shop.models import Produto
# c = Categoria.objects.get(id=1)
# c.get_absolute_path()
# '/computador/'

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagem = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)

    class Meta:
        db_table = 'produto'

    def get_absolute_path(self):
        return reverse('produto:exibe_produto', args=[self.id, self.slug])

    def __str__(self):
        return self.nome

# A view abaixo é utilizada para exibir um determinado produto
# Este URLconf trata requisições para http://localhost:8000/6/smartphone-samsung-galaxy-s8-plus/
# path('<int:id>/<slug:slug_do_produto>/', views.exibe_produto, name='exibe_produto'),
# /5/smartphone-samsung-galaxy-s8-plus/
# /4/smartphone-samsung-galaxy-s8/
# /2/computador-com-monitor-led-19-5-easypc-intel-core-i5-8gb-hd-1tb/

# from shop.models import Produto
# produto = Produto.objects.get(id=1)
# produto.get_absolute_path()
# '/1/notebook-del-vostro-3458-i3/'
