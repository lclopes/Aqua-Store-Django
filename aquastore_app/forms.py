from django import forms
from django.forms import ModelForm, Form
from aquastore_app.models import Agua

class AguaForm(ModelForm):
    class Meta:
        model = Agua
        fields = ['categoria', 'nome', 'slug', 'imagem', 'descricao', 'preco', 'estoque', 'disponivel']