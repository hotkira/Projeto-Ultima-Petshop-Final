from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField,
    ValidationError,
    HyperlinkedModelSerializer,
)

from reserva.models import ReservaDeBanho, Petshop
from base.models import Contato, CategoriaAnimal, CategoriaBanho, Cliente
from datetime import date


class PetshopModelSerializer(ModelSerializer):
    # Serializador para o modelo Petshop
    # Inclui a relação de reservas como hiperlinks para detalhes de reservas
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'
    )

    class Meta:
        model = Petshop
        fields = '__all__'


class PetshopNestedModelSerializer(ModelSerializer):
    # Serializador aninhado para o modelo Petshop
    # Inclui todos os campos do modelo
    class Meta:
        model = Petshop
        fields = '__all__'


class PetshopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    # Campo personalizado relacionado a Petshop
    # Usa o serializador PetshopNestedModelSerializer para representar objetos relacionados
    def __init__(self, **kwargs):
        self.serializer = PetshopNestedModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):

        return self.serializer(value, context=self.context).data


class AgendamentoModelSerializer(ModelSerializer):
    # Serializador para o modelo ReservaDeBanho
    # Usa o campo personalizado PetshopRelatedFieldCustomSerializer para representar a relação com Petshop
    # Inclui uma validação que verifica se a data da reserva não é no passado
    petshop = PetshopRelatedFieldCustomSerializer(
        queryset=Petshop.objects.all(),
        read_only=False
    )

    def validate_diaDaReserva(self, value):
        hoje = date.today()
        if value < hoje:
            raise ValidationError(
                'Não é permitido agendamentos com data para o passado')
        return value

    class Meta:
        model = ReservaDeBanho
        fields = '__all__'


class ContatoModelSerializer(ModelSerializer):
    # Serializador para o modelo Contato
    # Inclui todos os campos do modelo e é usado para representar detalhes de contatos
    class Meta:
        model = Contato
        fields = '__all__'


class ClienteModelSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'  # Inclua os campos relevantes do modelo


class CategoriaAnimalModelSerializer(ModelSerializer):
    class Meta:
        model = CategoriaAnimal
        fields = '__all__'  # Inclua os campos relevantes do modelo


class CategoriaBanhoModelSerializer(ModelSerializer):
    class Meta:
        model = CategoriaBanho
        fields = '__all__'  # Inclua os campos relevantes do modelo


class ReservaDeBanhoSerializer(HyperlinkedModelSerializer):
    cliente = ClienteModelSerializer
    petshop = PetshopModelSerializer
    categoriaAnimal = CategoriaAnimalModelSerializer
    categoriaBanho = CategoriaBanhoModelSerializer

    class Meta:
        model = ReservaDeBanho
        fields = '__all__'
