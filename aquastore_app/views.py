from django.shortcuts import render, get_object_or_404, redirect
from .models import CategoriaAguas, Agua
from aquastore_app.forms import AguaForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def lista_aguas(request, slug_da_categoria=None):
   categoria = None
   categorias = CategoriaAguas.objects.all().order_by("nome")
   aguas = Agua.objects.filter(disponivel=True).order_by("nome")

   if slug_da_categoria:
      categoria = get_object_or_404(CategoriaAguas, slug=slug_da_categoria)
      aguas = aguas.filter(categoria=categoria).order_by("nome")

   paginator = Paginator(aguas, 8)
   page = request.GET.get('page')
   try:
       aguas_lista = paginator.page(page)
   except PageNotAnInteger:
       # If page is not an integer deliver the first page
       aguas_lista = paginator.page(1)
   except EmptyPage:
       # If page is out of range deliver last page of results
       aguas_lista = paginator.page(paginator.num_pages)

   return render(request, 'aquastore_app/lista.html', {'categorias': categorias,
                                                       'page':page,
                                                 'aguas_lista': aguas_lista,
                                                 'categoria': categoria})

def exibe_agua(request, id, slug_da_agua):
   agua = get_object_or_404(Agua, id=id)
   return render(request, 'aquastore_app/exibe.html', {'agua': agua})


def sobre(request):
    return render(request, 'aquastore_app/sobre.html')

def cadastro(request):
    return render(request, 'aquastore_app/cadastro.html')

def admin(request):
    return render(request, 'aquastore_app/admin.html')

#@login_required(login_url='/autenticacao')
def novo(request):
    form = AguaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'aquastore_app/cadastro.html', {'form': form})
