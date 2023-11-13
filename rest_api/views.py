from django.shortcuts import render
from base.models import Contato
from rest_api.serializers import AgendamentoModelSerializer, ContatoModelSerializer, PetshopModelSerializer
from reserva.models import ReservaDeBanho, Petshop
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

# Definição de uma ViewSet para o modelo Petshop


class PetshopModelViewSet(ReadOnlyModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

# Definição de uma ViewSet para o modelo ReservaDeBanho


class AgendamentoModelViewSet(ModelViewSet):
    queryset = ReservaDeBanho.objects.all()
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

# Definição de uma ViewSet para o modelo Contato


class ContatoModelViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

# View para responder a requisições GET e POST para "/hello_world"


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        nome = request.data.get('nome')
        return Response({"mensagem": f'Olá, {nome}!!'})

    return Response({'Hello': 'hello world!'})

# View para responder a requisições GET para "/listar_contatos"


@api_view(['GET'])
def listar_contatos(request):
    contatos = Contato.objects.all()
    contatosFormatados = []

    for contato in contatos:
        contatosFormatados.append({
            "nome": contato.nome,
            "email": contato.email,
            "id": contato.id
        })

    return Response({'contatos': contatosFormatados})

# View para obter ou atualizar um contato pelo ID


@api_view(['GET', 'PUT'])
def obter_contato_pelo_id(request, id):
    contato = Contato.objects.filter(id=id)

    if len(contato) == 0:
        return Response({"mensagem": "Não foi encontrado nenhum contato com esse ID."})

    if request.method == 'PUT':
        nome = request.data.get('nome')
        email = request.data.get('email')
        mensagem = request.data.get('mensagem')

        contato[0].nome = nome
        contato[0].email = email
        contato[0].mensagem = mensagem

        contato[0].save()

        return Response({"contato": "contato atualizado"})

    contatoFormatado = {
        "nome": contato[0].nome,
        "email": contato[0].email,
        "mensagem": contato[0].mensagem,
        "id": contato[0].id
    }

    return Response({"contato": contatoFormatado})
