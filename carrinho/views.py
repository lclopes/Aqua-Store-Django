from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .carrinho import Carrinho
from .forms import QuantidadeForm, RemoveProdutoDoCarrinhoForm
from aquastore_app.models import Agua
from aquastore_app.views import lista_aguas

@login_required(login_url='/autenticacao/login')
def exibe_produtos_e_carrinho(request):
    return render(request, 'carrinho/vendas.html')

@login_required(login_url='/autenticacao/login')
def exibe_produtos(request):
    produtos = Agua.objects.all()
    lista_de_forms = []
    for p in produtos:
        lista_de_forms.append(QuantidadeForm(initial={'quantidade': 0}))

    return render(request, 'carrinho/produtos_a_venda.html',  {
        'listas': zip(produtos, lista_de_forms)
    })

@login_required(login_url='/autenticacao/login')
def exibe_carrinho(request):
    carrinho = Carrinho(request)

    lista_de_produtos_no_carrinho = carrinho.get_produtos()

    valoresInd = []
    for item in lista_de_produtos_no_carrinho:
        valoresInd.append(int(item['quantidade']) * Decimal(item['preco']))

    produtos_no_carrinho = []
    lista_de_forms = []
    valor_do_carrinho = 0
    for item in lista_de_produtos_no_carrinho:
        produtos_no_carrinho.append(item['produto'])
        lista_de_forms.append(QuantidadeForm(initial={'quantidade': item['quantidade']}))
        valor_do_carrinho = valor_do_carrinho + int(item['quantidade']) * Decimal(item['preco'])

    return render(request, 'carrinho/produtos_no_carrinho.html',  {
        'listas': zip(produtos_no_carrinho, lista_de_forms, valoresInd),
        'valor_do_carrinho': valor_do_carrinho,
    })

@login_required(login_url='/autenticacao/login')
def adicionar_ao_carrinho(request):
    form = QuantidadeForm(request.POST)
    if form.is_valid():
        quantidade = form.cleaned_data['quantidade']
        produto_id = form.cleaned_data['produto_id']

        carrinho = Carrinho(request)
        carrinho.adicionar(produto_id, quantidade)

        return exibe_carrinho(request)
    else:
        print(form.errors)
        raise ValueError('Ocorreu um erro inesperado ao adicionar um produto ao carrinho.')


@login_required(login_url='/autenticacao/login')
def adicionar_produto(request, id):
    produto_id = id

    carrinho = Carrinho(request)
    carrinho.adicionar(produto_id, 1)

    return lista_aguas(request)


@login_required(login_url='/autenticacao/login')
def remove_produto_carrinho(request):
    form = RemoveProdutoDoCarrinhoForm(request.POST)
    if form.is_valid():
        carrinho = Carrinho(request)
        carrinho.remover(form.cleaned_data['produto_id'])

        return exibe_carrinho(request)
    else:
        print(form.errors)
        raise ValueError('Ocorreu um erro inesperado ao adicionar um produto ao carrinho.')

@login_required(login_url='/autenticacao/login')
def atualiza_qtd_carrinho(request):
    form = QuantidadeForm(request.POST)
    if form.is_valid():
        produto_id = form.cleaned_data['produto_id']
        quantidade = form.cleaned_data['quantidade']

        carrinho = Carrinho(request)
        carrinho.alterar(produto_id, quantidade)

        return exibe_carrinho(request)
    else:
        print(form.errors)
        raise ValueError('Ocorreu um erro inesperado ao adicionar um produto ao carrinho.')
