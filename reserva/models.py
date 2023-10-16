from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from base.models import *
# Create your models here.
class ReservaDeBanho(models.Model):
    TAMANHO_OPCOES = (
        (0, 'Pequeno'),
        (1, 'Médio'),
        (2, 'Grande')
    )
    TURNO_OPCOES = (
        ('manha', 'Manhã'),
        ('tarde', 'Tarde')
    )
    STATUS_OPCOES = (
        ('agendado', 'Agendado'),
        ('cancelado', 'Cancelado'),
        ('concluido', 'Concluído'),
    )
    
    Cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name='Cliente',
        blank=True,
        null=True
    )
    nomeDoPet = models.CharField(verbose_name='Nome do PET', max_length=50)
    diaDaReserva = models.DateField(verbose_name='Dia da Reserva')
    observacoes = models.TextField(verbose_name='Observações', blank=True)
    
    categoriaAnimal = models.ForeignKey(
        CategoriaAnimal, 
        on_delete=models.CASCADE,
        verbose_name='Categoria de Animal',
        blank=True,
        null=True
    )
    
    turno = models.CharField(verbose_name='Turno', choices=TURNO_OPCOES, max_length=5)
    tamanho = models.IntegerField(verbose_name='Tamanho', choices=TAMANHO_OPCOES)
    
    racaAnimal = models.ForeignKey(
        RacaAnimal, 
        on_delete=models.CASCADE,
        verbose_name='Raça do Animal',
        blank=True,
        null=True
    )
    
    categoriaBanho = models.ForeignKey(
        CategoriaBanho, 
        on_delete=models.CASCADE,
        verbose_name='Categoria de Banho',
        blank=True,
        null=True
    )

    petshop = models.ForeignKey(
        'Petshop',
        related_name='reservas',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Formulário de Reserva de Banho'
        verbose_name_plural = 'Formulários de Reservas de Banhos'

    def __str__(self):
        return f'Nome do PET: {self.nomeDoPet} - Dia: {self.diaDaReserva} - Turno: {self.turno}'


class Petshop(models.Model):
  nome = models.CharField(verbose_name='Petshop', max_length=50)
  rua = models.CharField(verbose_name='Endereço', max_length=100)
  numero = models.CharField(verbose_name='Número', max_length=10)
  bairro = models.CharField(verbose_name='Bairro', max_length=50)

  class Meta:
    ordering = ['id']

  def qtd_reservas(self):
    return self.reservas.count()
  
  
  
  