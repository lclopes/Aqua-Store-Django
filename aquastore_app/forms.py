from django import forms
from django.forms import ModelForm, Form
from aquastore_app.models import Agua

class BuscaAguasForm(forms.Form):
   class Meta:
      fields = ('busca_por')

   busca_por = forms.CharField(
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
      required=False)

class AguaForm(ModelForm):
    class Meta:
        model = Agua
        fields = ['nome', 'categoria',  'imagem', 'descricao', 'preco', 'estoque', 'disponivel']

