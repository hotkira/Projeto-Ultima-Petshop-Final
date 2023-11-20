from pytest_django.asserts import assertTemplateUsed
from datetime import date, timedelta
import pytest
from base.models import Cliente
from model_bakery import baker
from reserva.models import Petshop, CategoriaAnimal, CategoriaBanho
from django.contrib.auth import get_user_model

# Fixtures

User = get_user_model()

# Fixture para criar dados de reserva válidos


@pytest.fixture
def reserva_valida():
    data = date.today()

    # uma instância de Petshop com id=2
    petshop = baker.make(Petshop)
    # instâncias de categoriaAnimal e categoriaBanho usando o baker
    categoria_animal = baker.make(CategoriaAnimal, nome='Cachorro')
    categoria_banho = baker.make(
        CategoriaBanho, nome='Banho Padrão', preco=15.50)

    dados = {
        'nomeDoPet': 'Jack',
        'email': 'tal@tal.com',
        'diaDaReserva': data,
        'observacoes': '',
        'turno': 'manha',
        'tamanho': 0,
        'categoriaAnimal': categoria_animal.pk,
        'categoriaBanho': categoria_banho.pk,
        'cliente_id': 1,
        'petshop': petshop.pk,
    }
    return dados

# Fixture para criar dados de reserva inválidos


@pytest.fixture
def reserva_invalida():
    data = date.today() - timedelta(days=1)
    petshop = baker.make(Petshop)
    categoria_animal = baker.make(CategoriaAnimal, nome='Cachorro')
    categoria_banho = baker.make(
        CategoriaBanho, nome='Banho Padrão', preco=15.50)
    dados = {
        'nomeDoPet': 'Jack',
        'email': 'tal@tal.com',
        'diaDaReserva': data,
        'observacoes': '',
        'turno': 'manha',
        'tamanho': 0,
        'categoriaAnimal': categoria_animal.pk,
        'categoriaBanho': categoria_banho.pk,
        'petshop': petshop.pk,
    }
    return dados

# Fixture para criar um cliente autenticado


@pytest.fixture
def authenticated_client(client):
    # Cria um usuário
    user = User.objects.create_user(
        username='Teste',
        password='senha',
        email='emailo@email.com'
    )

    # Autentica o cliente
    client.login(username='Teste', password='senha')

    return client

# Tests

# Teste para verificar se a criação de reserva retorna o template correto


@pytest.mark.django_db
def test_reserva_criar_deve_retornar_template_correto(authenticated_client):
    response = authenticated_client.get('/reserva/criar/')
    assert response.status_code == 200
    # Altere o nome do template aqui
    assertTemplateUsed(response, 'reserva_de_banhos.html')

# Teste para verificar se a reserva é criada com sucesso


# @pytest.mark.django_db
# def test_reserva_criada_com_sucesso(authenticated_client, reserva_valida):

#     response = authenticated_client.post('/reserva/criar/')
#     assert response.status_code == 200
#     assert 'Reserva feita com sucesso!' in str(response.content)


# Teste para verificar se a reserva não pode ser feita para uma data no passado


@pytest.mark.django_db
def test_reserva_data_no_passado(authenticated_client, reserva_invalida):
    response = authenticated_client.post('/reserva/criar/', reserva_invalida)
    assert 'Não é possível reservar para uma data no passado.' in response.content.decode(
        'utf-8')
