from django.shortcuts import render, redirect
from .forms import ReservaDeBanhoForm, ClienteForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


from django.shortcuts import render, redirect
from .forms import RegistrationForm


def login_view(request):
    error_message = 'Não foi possível carregar a página de login. Por favor, tente novamente.'
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('pagina_inicial')
        else:
            error_message = "Usuário ou senha inválidos. Por favor, tente novamente."

    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form, 'error_message': error_message})
    
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faça o login automaticamente após o registro
            return redirect('inicio')  # Redirecione para a página inicial após o registro
    else:
        form = RegistrationForm()
      
    return render(request, 'registration/registrar_cliente.html', {'form': form})

def inicio(request):
  return render(request, 'index.html')

def contato(request):
  print('método: ',request.method)
  sucesso = False

def reservaDeBanho(request):
    sucesso = False

    if request.method == 'POST':
        form = ReservaDeBanhoForm(request.POST)
        if form.is_valid():
            form.save()
            sucesso = True
    else:
        form = ReservaDeBanhoForm()

    titulo_pagina = "Reserva de banho"
    return render(request, 'reserva_de_banhos.html', {'form': form, 'sucesso': sucesso, 'titulo_pagina': titulo_pagina})


def cadastrar_cliente(request):
    sucesso = False  # Inicialmente, definimos sucesso como False

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            sucesso = True  # Se o cadastro for bem-sucedido, definimos sucesso como True
    else:
        form = ClienteForm()  # Use o nome correto do formulário aqui

    # Definindo o título da página
    titulo_pagina = "Cadastro de Cliente"
    return render(request, 'cadastro_cliente.html', {'cliente_form': form, 'sucesso': sucesso})
  
