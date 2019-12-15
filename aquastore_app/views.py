from django.db.models import Sum, F, FloatField
from django.http import QueryDict, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import CategoriaAguas, Agua
from aquastore_app.forms import AguaForm, BuscaAguasForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,    login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime


def lista_aguas(request, slug_da_categoria=None):
    categoria = None
    categorias = CategoriaAguas.objects.all().order_by("nome")
    aguas = Agua.objects.filter(disponivel=True).order_by("id")

    if slug_da_categoria:
        categoria = get_object_or_404(CategoriaAguas, slug=slug_da_categoria)
        aguas = aguas.filter(categoria=categoria).order_by("nome")

    busca = request.GET.get('busca_por')
    form = BuscaAguasForm()

    if busca:
        aguas = aguas.filter(nome__icontains=busca)

    qtdElem = aguas.count()

    paginator = Paginator(aguas, 12)
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
                                                        'qtdElem': qtdElem,
                                                        'busca': busca,
                                                        'aguas_lista': aguas_lista,
                                                        'categoria': categoria,
                                                        'form': form})


def exibe_agua(request, id):
    agua = Agua.objects.get(id=id)
    return render(request, 'aquastore_app/exibe.html', {'agua': agua})


def sobre(request):
    return render(request, 'aquastore_app/sobre.html')


def cadastro(request):
    return render(request, 'aquastore_app/cadastro.html')


@login_required
def admin(request):
    return render(request, 'aquastore_app/admin.html')

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
    return redirect('/')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')

###############################################################################################
