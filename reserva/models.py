from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from base.models import *


class ReservaDeBanho(models.Model):
    # Opções para o tamanho do animal
    TAMANHO_OPCOES = (
        (0, 'Pequeno'),
        (1, 'Médio'),
        (2, 'Grande')
    )

    # Opções para o turno da reserva
    TURNO_OPCOES = (
        ('manha', 'Manhã'),
        ('tarde', 'Tarde')
    )

    # Opções para o status da reserva
    STATUS_OPCOES = (
        ('agendado', 'Agendado'),
        ('cancelado', 'Cancelado'),
        ('concluido', 'Concluído'),
    )

    # Relacionamento com o cliente (opcional)
    cliente = models.ForeignKey(
        'base.Cliente',
        related_name='cliente',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    # Relacionamento com o petshop
    petshop = models.ForeignKey(
        'Petshop',
        related_name='reservas',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    # Nome do pet
    nomeDoPet = models.CharField(verbose_name='Nome do PET', max_length=50)

    # Data da reserva
    diaDaReserva = models.DateField(verbose_name='Dia da Reserva')

    # Observações (opcional)
    observacoes = models.TextField(verbose_name='Observações', blank=True)

    # Categoria de animal (opcional)
    categoriaAnimal = models.ForeignKey(
        CategoriaAnimal,
        on_delete=models.CASCADE,
        verbose_name='Categoria de Animal',
        blank=True,
        null=True
    )

    # Turno da reserva
    turno = models.CharField(verbose_name='Turno',
                             choices=TURNO_OPCOES, max_length=5)

    # Tamanho do animal
    tamanho = models.IntegerField(
        verbose_name='Tamanho', choices=TAMANHO_OPCOES)

    # Categoria de banho (opcional)
    categoriaBanho = models.ForeignKey(
        CategoriaBanho,
        on_delete=models.CASCADE,
        verbose_name='Categoria de Banho',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Formulário de Reserva de Banho'
        verbose_name_plural = 'Formulários de Reservas de Banhos'

    def __str__(self):
        return f'Nome do PET: {self.nomeDoPet} - Dia: {self.diaDaReserva} - Turno: {self.turno}'

# Modelo para representar um Petshop


class Petshop(models.Model):
    nome = models.CharField(verbose_name='Petshop', max_length=50)
    rua = models.CharField(verbose_name='Endereço', max_length=100)
    numero = models.CharField(verbose_name='Número', max_length=10)
    bairro = models.CharField(verbose_name='Bairro', max_length=50)

    class Meta:
        ordering = ['id']

    # Método para contar a quantidade de reservas associadas a este petshop
    def qtd_reservas(self):
        return self.reservas.count()

    def __str__(self):
        return self.nome
