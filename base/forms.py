from django import forms
from base.models import ReservaDeBanhoBase, Contato, CustomUser
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class ContatoForm(forms.ModelForm):
  class Meta:
    model = Contato
    fields = ['nome', 'email', 'mensagem']

class ReservaDeBanhoForm(forms.ModelForm):
  class Meta:
    model = ReservaDeBanhoBase
    fields = ['nomeDoPet', 'telefone', 'diaDaReserva', 'observacoes']
    widgets = {
      'diaDaReserva': forms.DateInput(attrs={'type': 'date'}),
    }
  
  
class ClienteForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nome', 'cpf', 'endereco', 'email', 'telefone', 'telefone2']
        
class RegistrationForm(UserCreationForm):
    # Adicione os campos personalizados do modelo CustomUser
    nome = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=14, required=True)
    endereco = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(max_length=100, required=True)
    telefone = forms.CharField(max_length=15, required=True)
    telefone2 = forms.CharField(max_length=15, required=False)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('nome', 'cpf', 'endereco', 'email', 'telefone', 'telefone2')