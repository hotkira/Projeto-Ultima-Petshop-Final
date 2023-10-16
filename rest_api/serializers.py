from rest_framework.serializers import ( 
  ModelSerializer, 
  HyperlinkedRelatedField, 
  PrimaryKeyRelatedField,
  ValidationError
)


from reserva.models import ReservaDeBanho, Petshop
from base.models import Contato
from datetime import date

class PetshopModelSerializer(ModelSerializer):
  reservas = HyperlinkedRelatedField(
    many=True,
    read_only=True,
    view_name='api:reserva-detail'
  )

  class Meta:
    model = Petshop
    fields = '__all__'


class PetshopNestedModelSerializer(ModelSerializer):
  class Meta:
    model = Petshop
    fields = '__all__'


class PetshopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
  def __init__(self, **kwargs):
    self.serializer = PetshopNestedModelSerializer
    super().__init__(**kwargs)

  def use_pk_only_optimization(self):
    return False
  
  def to_representation(self, value):
    return self.serializer(value, context=self.context).data


class AgendamentoModelSerializer(ModelSerializer):
  petshop = PetshopRelatedFieldCustomSerializer(
    queryset=Petshop.objects.all(),
    read_only=False
  )

  def validate_diaDaReserva(self, value):
    hoje = date.today()
    if value < hoje:
      raise ValidationError('Nao e permitido agendamentos com data para o passado')
    return value

  class Meta:
    model = ReservaDeBanho
    fields = '__all__'

class ContatoModelSerializer(ModelSerializer):
  class Meta:
    model = Contato
    fields = '__all__'