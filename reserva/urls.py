from django.urls import path

from reserva.views import criar_reserva_banho

app_name = 'reserva'

urlpatterns = [
  path('criar/', criar_reserva_banho, name='criar_reserva'),
]