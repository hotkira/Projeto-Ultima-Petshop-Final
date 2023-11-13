from pytest_django.asserts import assertTemplateUsed
from datetime import date, timedelta
import pytest
from base.models import Cliente
from model_bakery import baker
from reserva.models import ReservaDeBanho, Petshop
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
import re

# Fixtures

User = get_user_model()


@pytest.fixture
def reserva_valida():
    data = date.today()

    # Crie uma instância de Petshop com id=2
    petshop = baker.make(Petshop)

    dados = {
        'nomeDoPet': 'Jack',
        'email': 'tal@tal.com',
        'diaDaReserva': data,
        'observacoes': '',
        'turno': 'manha',
        'tamanho': 0,
        'categoriaAnimal': 1,
        'categoriaBanho': 1,
        'cliente_id': 1,
        'petshop': petshop.pk,
    }
    return dados


@pytest.fixture
def reserva_invalida():
    data = date.today() - timedelta(days=1)
    petshop = baker.make(Petshop)
    dados = {
        'nomeDoPet': 'Jack',
        'email': 'tal@tal.com',
        'diaDaReserva': data,
        'observacoes': '',
        'turno': 'manha',
        'tamanho': 0,
        'categoriaAnimal': 1,
        'categoriaBanho': 1,
        'petshop': petshop.pk,
    }
    return dados


@pytest.fixture
def authenticated_client(client):
    user = User.objects.create_user(
        username='seu_usuario',
        password='sua_senha',
        email='seu_email'  # Defina um email válido aqui
    )

    client.login(username='seu_usuario', password='sua_senha')
    return client

# Tests


@pytest.mark.django_db
def test_reserva_criar_deve_retornar_template_correto(authenticated_client):
    response = authenticated_client.get('/reserva/criar/')
    assert response.status_code == 200
    # Altere o nome do template aqui
    assertTemplateUsed(response, 'reserva_de_banhos.html')


# @pytest.mark.django_db
# def test_reserva_criada_com_sucesso(authenticated_client, reserva_valida):
#     response = authenticated_client.post('/reserva/criar/', reserva_valida)
#     print("Status Code:", response.status_code)
#     print("Response Content:", response.content)
#     assert response.status_code == 200
#     assert 'Reserva feita com sucesso!' in str(response.content)


@pytest.mark.django_db
def test_reserva_data_no_passado(authenticated_client, reserva_invalida):
    response = authenticated_client.post('/reserva/criar/', reserva_invalida)
    assert 'Não é possível reservar para uma data no passado.' in response.content.decode(
        'utf-8')
