import pytest
from datetime import date, timedelta
from rest_framework.test import APIClient
from model_bakery import baker
from reserva.models import Petshop, ReservaDeBanho
from rest_framework.reverse import reverse
from base.models import Cliente, CategoriaAnimal, CategoriaBanho

# Fixture para dados de agendamento inválidos


@pytest.fixture
def dados_agendamento_invalido():
    ontem = date.today() - timedelta(days=1)
    petshop = baker.make(Petshop)
    # Criação da categoria de animal com id=1
    categoria_animal = baker.make(CategoriaAnimal, id=1)
    # Criação da categoria de banho com id=1
    categoria_banho = baker.make(CategoriaBanho, id=1)
    agendamento = {
        'nomeDoPet': 'Jack',
        'diaDaReserva': ontem,
        'observacoes': '',
        'turno': 'manha',
        'tamanho': 0,
        'categoriaAnimal': categoria_animal.id,  # id da categoria criada
        'categoriaBanho': categoria_banho.id,  # id da categoria criada
        'petshop': petshop.pk,
    }
    return agendamento

# Fixture para dados de agendamento válidos


@pytest.fixture
def dados_agendamento_valido():
    hoje = date.today()
    petshop = baker.make(Petshop)
    # Crie a categoria de animal com id=1
    categoria_animal = baker.make(CategoriaAnimal, id=1)
    # Crie a categoria de banho com id=1
    categoria_banho = baker.make(CategoriaBanho, id=1)
    agendamento = {
        'nomeDoPet': 'Jack',
        'diaDaReserva': hoje,
        'observacoes': '',
        'turno': 'manha',
        'tamanho': 0,
        'categoriaAnimal': categoria_animal.id,  # Use o id da categoria criada
        'categoriaBanho': categoria_banho.id,  # Use o id da categoria criada
        'petshop': petshop.pk,
    }
    return agendamento

# Fixture para instância de agendamento válido


@pytest.fixture
def agendamento_valido_instancia():
    hoje = date.today()
    petshop = baker.make(Petshop)
    # Crie a categoria de animal com id=1
    categoria_animal = baker.make(CategoriaAnimal, id=1)
    # Crie a categoria de banho com id=1
    categoria_banho = baker.make(CategoriaBanho, id=1)
    agendamento = {
        'nomeDoPet': 'Jack',
        'diaDaReserva': hoje,
        'observacoes': '',
        'turno': 'manha',
        'tamanho': 0,
        'categoriaAnimal': categoria_animal,
        'categoriaBanho': categoria_banho,
        'petshop': petshop,
    }
    return agendamento

# Fixture para um usuário


@pytest.fixture
def usuario():
    return baker.make(Cliente)

# Teste para obter todos os petshops


@pytest.mark.django_db
def test_obter_petshop_lista_vazia():
    client = APIClient()
    resposta = client.get('/api/petshop/')

    assert len(resposta.data['results']) == 0

# Teste para obter um agendamento pelo ID


@pytest.mark.django_db
def test_obter_todos_petshops_com_pelo_menos_um_agendamento(dados_agendamento_valido):
    petshop = baker.make(Petshop)
    agendamento = baker.make(ReservaDeBanho, petshop=petshop)

    client = APIClient()
    # Use a função reverse para construir a URL
    url = reverse('api:petshop-list')
    resposta = client.get(url)

    assert len(resposta.data['results']) >= 1


@pytest.mark.django_db
def teste_de_agendamento(dados_agendamento_valido, usuario):
    client = APIClient()
    client.force_authenticate(usuario)
    resposta = client.post('/api/agendamento/', dados_agendamento_valido)
    if resposta.status_code != 201:
        print(resposta.data)

    assert resposta.status_code == 201


@pytest.mark.django_db
def test_obter_agendamento_pelo_id(agendamento_valido_instancia):
    ReservaDeBanho.objects.create(**agendamento_valido_instancia)

    client = APIClient()
    resposta = client.get('/api/agendamento/1/')

    assert resposta.json()['nomeDoPet'] == 'Jack'
    assert resposta.json()['turno'] == 'manha'

    assert resposta.status_code == 200


@pytest.mark.django_db
def test_remover_agendamento_pelo_codigo(agendamento_valido_instancia, usuario):

    agendamento_criado = ReservaDeBanho.objects.create(
        **agendamento_valido_instancia,
    )

    client = APIClient()
    client.force_authenticate(usuario)

    resposta_primeiro_cliente = client.get(
        f'/api/agendamento/{agendamento_criado.id}/')
    assert resposta_primeiro_cliente.json()['nomeDoPet'] == 'Jack'
    assert resposta_primeiro_cliente.status_code == 200

    # Teste para remover um agendamento pelo código
    client.delete(f'/api/agendamento/{agendamento_criado.id}/')
    resposta_segundo_get = client.get(
        f'/api/agendamento/{agendamento_criado.id}/')

    assert resposta_segundo_get.status_code == 404
