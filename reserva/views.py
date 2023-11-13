from django.shortcuts import render, redirect
from .forms import ReservaDeBanhoForm
from reserva.models import ReservaDeBanho
from django.contrib.auth.decorators import login_required
from base.models import Cliente


@login_required
def criar_reserva_banho(request):
    sucesso = False

    if request.method == 'POST':
        form = ReservaDeBanhoForm(request.POST)

        if form.is_valid():
            if request.user.is_authenticated:
                # Se o usuário estiver autenticado, associe a reserva ao cliente
                cliente = Cliente.objects.get(id=request.user.id)
                reserva = form.save(commit=False)
                reserva.cliente = cliente
                reserva.save()
                sucesso = True
            else:
                print('Usuário não autenticado')
        else:
            # O formulário não é válido, você pode lidar com isso aqui
            print('Formulário inválido:', form.errors)
    else:
        form = ReservaDeBanhoForm()

    titulo_pagina = "Reserva de banho"
    return render(request, 'reserva_de_banhos.html', {'form': form, 'sucesso': sucesso, 'titulo_pagina': titulo_pagina})
