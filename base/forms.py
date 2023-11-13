from django import forms
from base.models import ReservaDeBanhoBase, Contato, Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator

# Formulário de login


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

# Formulário para o modelo Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

# Formulário para o modelo ReservaDeBanhoBase


class ReservaDeBanhoForm(forms.ModelForm):
    class Meta:
        model = ReservaDeBanhoBase
        fields = ['nomeDoPet', 'telefone', 'diaDaReserva', 'observacoes']
        widgets = {
            'diaDaReserva': forms.DateInput(attrs={'type': 'date'}),
        }

# Formulário de registro de cliente


class ClienteRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Este será seu nome de usuário (email).'
    )
    nome = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=14)
    endereco = forms.CharField(max_length=200)
    telefone = forms.CharField(max_length=15)
    telefone2 = forms.CharField(max_length=15, required=False)

    class Meta:
        model = Cliente
        fields = ('email', 'password1', 'password2', 'nome',
                  'cpf', 'endereco', 'telefone', 'telefone2')

    def __init__(self, *args, **kwargs):
        super(ClienteRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'A senha deve conter pelo menos 8 caracteres.'

    def save(self, commit=True):
        user = super(ClienteRegistrationForm, self).save(commit=False)
        user.username = user.email  # Use o email como nome de usuário
        if commit:
            user.save()
        return user

# Formulário de cliente (com opção de fornecer um nome de usuário personalizado)


class ClienteForm(UserCreationForm):
    nome = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=14)
    endereco = forms.CharField(max_length=200)
    email = forms.EmailField()
    telefone = forms.CharField(max_length=15)
    telefone2 = forms.CharField(max_length=15, required=False)
    username = forms.CharField(
        max_length=30,
        required=False,  # Campo é opcional
        validators=[UnicodeUsernameValidator()],
        help_text=("Campo de nome de usuário (opcional). "
                   "Deixe em branco para usar o email como nome de usuário.")
    )

    class Meta:
        model = Cliente
        fields = ['username', 'password1', 'password2', 'nome',
                  'cpf', 'endereco', 'email', 'telefone', 'telefone2']
