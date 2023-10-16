from django.shortcuts import render, redirect
from .forms import ReservaDeBanhoForm




def criar_reserva_banho(request):

    sucesso = False  # Inicialmente, definimos sucesso como False

    if request.method == 'POST':
        form = ReservaDeBanhoForm(request.POST)
        if form.is_valid():
            
            form.save()
            sucesso = True
    else:
        form = ReservaDeBanhoForm()

    # Definindo o título da página
    titulo_pagina = "Reserva de banho"
    return render(request, 'reserva_de_banhos.html', {'form': form, 'sucesso': sucesso, 'titulo_pagina': titulo_pagina})
