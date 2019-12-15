from django import forms
from django.core.validators import RegexValidator
from django.forms import ModelForm
from aquastore_app.models import Agua, CategoriaAguas


class BuscaAguasForm(forms.Form):
    class Meta:
        fields = ('busca_por')

    busca_por = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control shadow-sm', 'maxlength': '120', 'placeholder': 'Busque por algum produto específico '}),
        required=False)


class AguaForm(ModelForm):
    class Meta:
        model = Agua
        fields = ['nome', 'categoria', 'imagem', 'descricao', 'preco', 'estoque', 'disponivel']

    nome = forms.CharField(
        error_messages={'required': 'Campo obrigatório.',
                        'unique': 'Produto duplicado.'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True)

    categoria = forms.ModelChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        queryset=CategoriaAguas.objects.all().order_by('nome'),
        empty_label='--- Selecione uma categoria ---',
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    imagem = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True)

    descricao = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=False)

    preco = forms.DecimalField(
        localize=True,
        error_messages={'required': 'Campo obrigatório.', },
        validators=[RegexValidator(regex='^[0-9]{1,7}(,[0-9]{2})?$', message="Informe o valor no formato 9999999,99.")],
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm',
                                      'maxlength': '10',
                                      'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)'
                                                    ' || event.charCode == 44'}),
        required=True)

    estoque = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True)

    disponivel = forms.BooleanField()


