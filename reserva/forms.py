from django import forms
from datetime import date
from reserva.models import ReservaDeBanho, Petshop,CategoriaAnimal, RacaAnimal, CategoriaBanho

class ReservaDeBanhoForm(forms.ModelForm):
    categoriaAnimal = forms.ModelChoiceField(
        queryset=CategoriaAnimal.objects.all(),
        required=False,
        label='Categoria de Animal'
    )
    
    racaAnimal = forms.ModelChoiceField(
        queryset=RacaAnimal.objects.all(),
        required=False,
        label='Raça do Animal'
    )
    
    categoriaBanho = forms.ModelChoiceField(
        queryset=CategoriaBanho.objects.all(),
        required=False,
        label='Categoria de Banho'
    )
    
    petshop = forms.ModelChoiceField(
        queryset=Petshop.objects.all(),
        required=False,
        label='Petshop'
    )

    class Meta:
        model = ReservaDeBanho
        fields = ['nomeDoPet', 'diaDaReserva', 'turno', 'tamanho', 'observacoes']
        widgets = {
            'diaDaReserva': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_diaDaReserva(self):
        print('Início da validação personalizada')
        diaDaReservaSelecionado = self.cleaned_data['diaDaReserva']
        hoje = date.today()

        if diaDaReservaSelecionado < hoje:
            raise forms.ValidationError('Não é possível reservar para uma data no passado.')

        quantidadeDeReservasParaODiaSelecionado = ReservaDeBanho.objects.filter(diaDaReserva=diaDaReservaSelecionado).count()
        print(f'Quantidade de reservas para o dia: {quantidadeDeReservasParaODiaSelecionado}')
        if quantidadeDeReservasParaODiaSelecionado >= 4:
            raise forms.ValidationError('O limite máximo de reservas para este dia já foi atingido. Escolha outra data.')

        return diaDaReservaSelecionado
