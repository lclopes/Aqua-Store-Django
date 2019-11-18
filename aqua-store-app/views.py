from django.shortcuts import render, get_object_or_404
from .models import CategoriaAguas, Agua
import os


def lista_aguas(request, slug_da_categoria=None):
   categoria = None
   categorias = CategoriaAguas.objects.all().order_by("nome")
   aguas = Agua.objects.filter(disponivel=True).order_by("nome")
   if slug_da_categoria:
      categoria = get_object_or_404(CategoriaAguas, slug=slug_da_categoria)
      aguas = aguas.filter(categoria=categoria).order_by("nome")

   return render(request, 'aqua-store-app/lista.html', {'categorias': categorias,
                                                 'aguas': aguas,
                                                 'categoria': categoria})


def exibe_agua(request, id, slug_da_agua):
   agua = get_object_or_404(Agua, id=id)
   return render(request, 'aqua-store-app/exibe.html', {'agua': agua})


def sobre(request):
    return render(request, 'aqua-store-app/sobre.html')
