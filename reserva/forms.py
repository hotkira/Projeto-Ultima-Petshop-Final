from django import forms
from datetime import date
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from base.models import Cliente
from reserva.models import ReservaDeBanho, Petshop, CategoriaAnimal, CategoriaBanho

# Definição do formulário para criar ou editar uma reserva de banho


class ReservaDeBanhoForm(forms.ModelForm):
    # Campos para escolher a categoria de animal, categoria de banho e petshop
    TAMANHO_OPCOES = (
        (0, 'Pequeno'),
        (1, 'Médio'),
        (2, 'Grande')
    )

    categoriaAnimal = forms.ModelChoiceField(
        queryset=CategoriaAnimal.objects.all(),
        required=False,
        label='Categoria de Animal',
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial=None  # Defindo o valor inicial como None
    )

    categoriaBanho = forms.ModelChoiceField(
        queryset=CategoriaBanho.objects.all(),
        required=False,
        label='Categoria de Banho',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    petshop = forms.ModelChoiceField(
        queryset=Petshop.objects.all(),
        required=False,
        label='Petshop',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    tamanho = forms.ChoiceField(
        choices=[('', 'Escolha o tamanho')] +
        list(ReservaDeBanho.TAMANHO_OPCOES),
        required=True,
        label='Tamanho',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(ReservaDeBanhoForm, self).__init__(*args, **kwargs)
        # Defina a data inicial (hoje) para o campo diaDaReserva
        self.fields['diaDaReserva'].initial = date.today()

    class Meta:
        model = ReservaDeBanho
        fields = ['petshop', 'nomeDoPet', 'tamanho', 'categoriaAnimal',
                  'categoriaBanho', 'diaDaReserva', 'turno', 'observacoes']
        widgets = {
            'diaDaReserva': forms.DateInput(attrs={'type': 'date'}),
        }
    # Função para validar os campos do formulário

    def clean(self):
        cleaned_data = super().clean()
        for field_name, field_value in list(cleaned_data.items()):
            if not field_value and field_name != 'observacoes':
                self.add_error(field_name, 'Este campo é obrigatório.')

    def clean_diaDaReserva(self):
        # Validando a data da reserva
       # print('inicio da validacao customizada')
        diaDaReservaSelecionado = self.cleaned_data['diaDaReserva']
        hoje = date.today()
        # Não deixa reservar para uma data no passado
        if diaDaReservaSelecionado < hoje:
            raise forms.ValidationError(
                'Não é possível reservar para uma data no passado.')

        quantidadeDeReservasParaODiaSelecionado = ReservaDeBanho.objects.filter(
            diaDaReserva=diaDaReservaSelecionado).count()
        # Definindo a quantidade de reservas para o dia selecionado
        if quantidadeDeReservasParaODiaSelecionado >= 10:
            raise forms.ValidationError(
                'O limite máximo de reservas para este dia já foi atingido. Escolha outra data.')

        return diaDaReservaSelecionado
