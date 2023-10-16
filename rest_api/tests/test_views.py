import pytest
from datetime import date, timedelta
from rest_framework.test import APIClient
from model_bakery import baker
from reserva.models import Petshop, ReservaDeBanho



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

@pytest.fixture
def dados_agendamento_valido():
  hoje = date.today()
  petshop = baker.make(Petshop)
  agendamento = {
    'nomeDoPet' : 'Jack',
    'telefone' : '998832569',
    'email' : 'tal@tal.com',
    'diaDaReserva' : hoje,
    'observacoes' : '',
    'turno' : 'manha',
    'tamanho' : 0,
    'petshop' : petshop.pk,
  }
  return agendamento
  
#para recevber todo petshop e não apenas a PK
@pytest.fixture
def agendamento_valido():
  hoje = date.today()
  petshop = baker.make(Petshop)
  agendamento = {
    'nomeDoPet' : 'Kako',
    'telefone' : '998832569',
    'email' : 'tal@tal.com',
    'diaDaReserva' : hoje,
    'observacoes' : '',
    'turno' : 'manha',
    'tamanho' : 0,
    'petshop' : petshop,
  }
  return agendamento
  
  
@pytest.fixture
def usuario(): 
  return baker.make('auth.User')

@pytest.mark.django_db
def test_obter_petshop_lists_vazia():
  client = APIClient()
  resposta = client.get('/api/petshop/')
  
  assert len(resposta.data['results']) == 0
  
@pytest.mark.django_db
def test_obter_todos_petshops_com_1_elemento(dados_agendamento_invalido):
  client = APIClient()
  resposta = client.get('/api/petshop/')
  
  assert len(resposta.data['results']) == 1
  
@pytest.mark.django_db  
def teste_de_agendamento(dados_agendamento_valido, usuario):
  client = APIClient()
  client.force_authenticate(usuario)
  resposta = client.post('/api/agendamento/', dados_agendamento_valido)
  
  assert resposta.status_code == 201
  
@pytest.mark.django_db
def test_pegar_agendamento_pelo_codigo(agendamento_valido):
  # o ** é para pegar do dicionario
  ReservaDeBanho.objects.create(**agendamento_valido)
  client = APIClient()
  resposta = client.get('/api/agendamento/1/')
  assert resposta.json()['nomeDoPet'] == 'Kako'
  assert resposta.status_code == 200
  
@pytest.mark.django_db
def test_remover_agendamento_pelo_codigo(agendamento_valido, usuario):
  # o ** é para pegar do dicionario
  ReservaDeBanho.objects.create(**agendamento_valido)
  client = APIClient()
  client.force_authenticate(usuario)
  resposta_primeiro_cliente = client.get('/api/agendamento/1/')
  assert resposta_primeiro_cliente.json()['nomeDoPet'] == 'Kako'
  assert resposta_primeiro_cliente.status_code == 200
  
  #remover
  client.delete('/api/agendamento/1/')
  respostaSegundoGet = client.get('/api/agendamento/1/')
  
  assert respostaSegundoGet.status_code == 404