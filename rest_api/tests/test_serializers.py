import pytest
from datetime import date, timedelta
from rest_framework.test import APIClient
from model_bakery import baker
from reserva.models import Petshop
from reserva.models import ReservaDeBanho
from rest_api.serializers import AgendamentoModelSerializer


@pytest.fixture
def dados_agendamento_invalido():
    ontem = date.today() - timedelta(days=1)
    petshop = baker.make(Petshop)
    agendamento = {
        'nomeDoPet': 'Jack',
        'email': 'tal@tal.com',
        'diaDaReserva': ontem,
        'observacoes': '',
        'turno': 'manha',
        'tamanho': 0,
        'categoriaAnimal': 1,
        'categoriaBanho': 1,
        'petshop': petshop.pk,
    }
    return agendamento


@pytest.mark.django_db
def test_agendamento_invalido(dados_agendamento_invalido):
    serializer = AgendamentoModelSerializer(data=dados_agendamento_invalido)
    assert not serializer.is_valid(
    ), "O serializer deveria ser inválido devido à data no passado"
    assert 'diaDaReserva' in serializer.errors, "O campo 'diaDaReserva' deve estar nos erros"
    assert serializer.errors['diaDaReserva'][0] == "Não é permitido agendamentos com data para o passado", "Mensagem de erro incorreta"
