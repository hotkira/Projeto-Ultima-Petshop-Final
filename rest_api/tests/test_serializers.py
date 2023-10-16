import pytest
from datetime import date, timedelta
from rest_framework.test import APIClient
from model_bakery import baker
from reserva.models import Petshop
from rest_api.serializers import AgendamentoModelSerializer

@pytest.fixture
def dados_agendamento_invalido():
  ontem = date.today() - timedelta(days=1)
  petshop = baker.make(Petshop)
  agendamento = {
    'nomeDoPet' : 'Jack',
    'telefone' : '998832569',
    'email' : 'tal@tal.com',
    'diaDaReserva' : ontem,
    'observacoes' : '',
    'turno' : 'manha',
    'tamanho' : 0,
    'petshop' : petshop.pk,
  }
  return agendamento

@pytest.mark.django_db
def teste_agendamento_invalido(dados_agendamento_invalido):
  serializer = AgendamentoModelSerializer(data=dados_agendamento_invalido)
  assert not serializer.is_valid()