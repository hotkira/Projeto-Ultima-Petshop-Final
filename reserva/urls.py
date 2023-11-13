from django.urls import path
from reserva.views import criar_reserva_banho

# Define um namespace para as URLs deste aplicativo
app_name = 'reserva'

# Lista de URLs do aplicativo 'reserva'
urlpatterns = [
    # Define uma URL para criar uma reserva de banho
    path('criar/', criar_reserva_banho, name='criar_reserva'),


]
