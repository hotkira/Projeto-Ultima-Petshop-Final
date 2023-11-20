import pytest
from reserva.models import ReservaDeBanho, Petshop
from model_bakery import baker
from datetime import date

# Fixture para criar uma reserva de exemplo


@pytest.fixture
def reserva():
    data = date(2023, 9, 27)
    reserva = baker.make(
        ReservaDeBanho,
        nomeDoPet='Jack',
        turno='tarde',
        diaDaReserva=data,
        observacoes='Teste observação para os banhos',
        tamanho=2
    )
    return reserva

# Exemplo de caso de teste para verificar se a configuração do teste está funcionando


def test_config():
    assert 1 == 1

# teste para verificar se a representação de string da reserva está conforme o esperado


@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada(reserva):
    assert str(reserva) == 'Nome do PET: Jack - Dia: 2023-09-27 - Turno: tarde'

# teste para verificar se os campos de observações e tamanho da reserva estão configurados corretamente


@pytest.mark.django_db
def test_campos_observacoes_e_tamanho_de_reserva(reserva):
    assert reserva.observacoes == 'Teste observação para os banhos'
    assert reserva.tamanho == 2

# teste para verificar a quantidade de reservas para um petshop


@pytest.mark.django_db
def test_qtd_de_reserva_do_petshop():
    # Criando uma instância de Petshop usando o baker
    petshop = baker.make(Petshop)

    # Definindo a quantidade desejada de reservas
    quantidade = 5

    # Criando várias reservas para o petshop
    baker.make(
        ReservaDeBanho,
        quantidade,
        petshop=petshop
    )

    # Verificando se a quantidade de reservas para o petshop está conforme o esperado
    assert petshop.qtd_reservas() == quantidade
