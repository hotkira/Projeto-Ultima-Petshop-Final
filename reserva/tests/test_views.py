from pytest_django.asserts import assertTemplateUsed
from datetime import date, timedelta
import pytest
from model_bakery import baker
from reserva.models import ReservaDeBanho

# Fixtures

@pytest.fixture
def reserva_valida():
  data = date.today()
  dados = {
    'nomeDoPet': 'Liz',
    'telefone': '8199998989',
    'email': 'liz@gmail.com',
    'diaDaReserva': data,
    'observacoes': 'Liz tá bastante suja!',
    'turno': 'tarde',
    'tamanho': 2
  }
  return dados

@pytest.fixture
def reserva_invalida():
  data = date.today() - timedelta(days=1)
  dados = {
    'nomeDoPet': 'Liz',
    'telefone': '8199998989',
    'email': 'liz@gmail.com',
    'diaDaReserva': data,
    'observacoes': 'Liz tá bastante suja!',
    'turno': 'tarde',
    'tamanho': 2
  }
  return dados

# Tests

def test_reserva_criar_deve_retornar_template_correto(client):
  response = client.get('/reserva/criar/')

  assert response.status_code == 200
  assertTemplateUsed(response, 'reserva_de_banho.html')

@pytest.mark.django_db
def test_reserva_criada_com_sucesso(client, reserva_valida):
  
  response = client.post('/reserva/criar/', reserva_valida)

  assert response.status_code == 200
  assert 'Reserva feita com sucesso!' in str(response.content)


@pytest.mark.django_db
def test_reserva_data_no_passado(client, reserva_invalida):
  
  response = client.post('/reserva/criar/', reserva_invalida)

  assert response.status_code == 200
  assert 'Nao e possivel reservar para uma data no passado.' in str(response.content)


@pytest.mark.django_db
def test_reserva_limite_maximo_atingido(client, reserva_valida):
  quantidade = 4
  baker.make(
    ReservaDeBanho,
    quantidade
  )

  response = client.post('/reserva/criar/', reserva_valida)

  assert response.status_code == 200
  assert 'O limite maximo de reservas para este dia ja foi atingido. Escolha outra data.' in str(response.content)


@pytest.mark.django_db
def test_se_reserva_esta_inserindo_no_banco_corretamente(client, reserva_valida):
  client.post('/reserva/criar/', reserva_valida)

  assert ReservaDeBanho.objects.all().count() == 1

  primeiraReservaNoBanco = ReservaDeBanho.objects.first()
  print(primeiraReservaNoBanco)

  assert primeiraReservaNoBanco.nomeDoPet == reserva_valida['nomeDoPet']
  assert primeiraReservaNoBanco.diaDaReserva == reserva_valida['diaDaReserva']
  assert primeiraReservaNoBanco.turno == reserva_valida['turno']