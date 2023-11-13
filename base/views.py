from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from .forms import LoginForm, ClienteRegistrationForm, ReservaDeBanhoForm, ClienteForm, ContatoForm
from base.models import Cliente
from django.contrib.auth.decorators import login_required
import logging

# Configuração para registrar logs e encontrar o cliente logado
logger = logging.getLogger(__name__)

# Função para a página de login


def login_view(request):
    error_message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            cliente = None  # Inicializa cliente com None

            try:
                cliente = Cliente.objects.get(username=username)
                user = authenticate(
                    request, username=username, password=password)
            except Cliente.DoesNotExist:
                pass

            if user is not None:
                return redirect(reverse('inicio'))

            error_message = "Usuário ou senha inválidos. Por favor, tente novamente."

    form = LoginForm()
    return render(request, 'registration/login.html', {'form': form, 'error_message': error_message})

# Função para o registro de cliente


def register(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()

            # Autenticar o usuário após o registro
            user = authenticate(username=cliente.username,
                                password=request.POST['password1'])
            if user is not None:
                login(request, user)

            return redirect('inicio')
    else:
        form = ClienteForm()

    return render(request, 'registration/registrar_cliente.html', {'form': form})

# Página de início


def inicio(request):
    logger.debug('This is a test log message for the inicio view')
    return render(request, 'index.html')

# Função para a página de contato


def contato(request):
    sucesso = False
    form = ContatoForm()

    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            sucesso = True
    titulo_pagina = "Contato"
    return render(request, 'contato.html', {'form': form, 'sucesso': sucesso, 'titulo_pagina': titulo_pagina})


# Função para reserva de banho (requer autenticação)


@login_required
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

# Função para cadastrar um cliente


def cadastrar_cliente(request):
    sucesso = False

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            sucesso = True
    else:
        form = ClienteForm()

    titulo_pagina = "Cadastro de Cliente"
    return render(request, 'cadastro_cliente.html', {'cliente_form': form, 'sucesso': sucesso})
