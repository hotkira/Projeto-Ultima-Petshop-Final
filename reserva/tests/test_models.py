import pytest
from reserva.models import ReservaDeBanho, Petshop
from model_bakery import baker
from datetime import date

@pytest.fixture
def reserva():
  data = date(2023, 9, 27)
  reserva = baker.make(
    ReservaDeBanho,
    nomeDoPet= 'Pingo',
    turno = 'tarde',
    diaDaReserva = data,
    email = 'fabio@gmail.com',
    observacoes = 'Pingo fica bastante agitado nos banhos!',
    tamanho = 2
  )
  return reserva

def test_config():
  assert 1 == 1

@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada(reserva):
  assert str(reserva) == 'Nome do PET: Pingo - Dia: 2023-09-27 - Turno: tarde'
  assert reserva.email == 'fabio@gmail.com'


@pytest.mark.django_db
def test_campos_observacoes_e_tamanho_de_reserva(reserva):
  assert reserva.observacoes == 'Pingo fica bastante agitado nos banhos!'
  assert reserva.tamanho == 2

@pytest.mark.django_db
def test_qtd_de_reserva_do_petshop():
  petshop = baker.make(Petshop)

  quantidade = 5

  baker.make(
    ReservaDeBanho,
    quantidade,
    petshop=petshop
  )

  assert petshop.qtd_reservas() == quantidade