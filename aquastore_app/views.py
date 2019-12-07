from django.shortcuts import render, get_object_or_404, redirect
from .models import CategoriaAguas, Agua
from aquastore_app.forms import AguaForm, BuscaAguasForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum, F, FloatField


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
                                                        'page': page,
                                                        'aguas_lista': aguas_lista,
                                                        'categoria': categoria})


def exibe_agua(request, id):
    agua = get_object_or_404(Agua, id=id)
    return render(request, 'aquastore_app/exibe.html', {'agua': agua})


def sobre(request):
    return render(request, 'aquastore_app/sobre.html')


def cadastro(request):
    return render(request, 'aquastore_app/cadastro.html')


def admin(request):
    return render(request, 'aquastore_app/admin.html')


def adminlist(request):
    aguas = Agua.objects.filter(disponivel=True).order_by("nome")
    busca = request.GET.get('busca_por')

    if busca:
        aguas = aguas.filter(nome__icontains=busca)

    qtdElem = aguas.count()

    paginator = Paginator(aguas, 4)
    page = request.GET.get('page')
    aguas = paginator.get_page(page)

    return render(request, 'aquastore_app/listaadmin.html', {'aguas': aguas,
                                                             'qtdElem': qtdElem,
                                                             'busca': busca})

# @login_required(login_url='/autenticacao')
def novo(request):
    form = AguaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'aquastore_app/cadastro.html', {'form': form})


def atualiza(request, id):
    agua = Agua.objects.get(id=id)
    form = AguaForm(request.POST or None, instance=agua)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'aquastore_app/cadastro.html', {'form': form})


def deleta(request, id):
    agua = Agua.objects.get(id=id)
    agua.delete()
    return redirect('/listaadmin.html')


def busca(request):
    form = BuscaAguasForm()
    return render(request, 'aquastore_app/busca.html', {
        'form': form
    })


def busca_aguas_lista(request):
    form = BuscaAguasForm(request.GET)
    if (form.is_valid()):
        busca_por = form.cleaned_data['busca_por']
        lista_de_aguas = Agua.objects.filter(nome__icontains=busca_por).order_by('nome')

        resultado = lista_de_aguas.aggregate(
            total=Sum(F('preco'), output_field=FloatField()))

        if resultado['total']:
            total = '{0:.2f}'.format(resultado['total'])
        else:
            total = '0,00'

        paginator = Paginator(lista_de_aguas, 5)
        pagina = request.GET.get('pagina')
        produtos = paginator.get_page(pagina)

        #      lista_de_forms = []
        #      for produto in produtos:
        #         lista_de_forms.append(RemoveProdutoForm(initial={'produto_id': produto.id}))

        lista_de_ids = []
        for produto in produtos:
            lista_de_ids.append(produto.id)

        return render(request, 'produto/pesquisa_produto.html', {
            'form': form,
            #        'listas': zip(produtos, lista_de_forms),
            'produtos': produtos,
            'lista_de_ids': lista_de_ids,
            'total': total,
            'busca_por': busca_por
        })

    else:
        raise ValueError('Ocorreu um erro inesperado ao tentar pesquisar um produto.')
