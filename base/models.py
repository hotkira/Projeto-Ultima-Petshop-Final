from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.validators import UnicodeUsernameValidator

# Modelo de usuário personalizado, estendendo o AbstractUser do Django


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group, related_name='other_users', blank=True,
        help_text="Os grupos aos quais este usuário pertence. Um usuário receberá todas as permissões concedidas a cada um de seus grupos.")
    user_permissions = models.ManyToManyField(
        Permission, related_name='other_users', blank=True,
        help_text="Permissões específicas para este usuário.")

# Modelo para formulários de contato


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False, blank=True)
    finalizado = models.BooleanField(
        verbose_name='Finalizado', default=False, blank=True)

    def __str__(self):
        return f'Nome: {self.nome} - Email: {self.email}'

    class Meta:
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contatos'
        ordering = ['-nome']

# Modelo para reservas de banho


class ReservaDeBanhoBase(models.Model):
    nomeDoPet = models.CharField(verbose_name='Nome do PET', max_length=50)
    telefone = models.CharField(verbose_name='Telefone', max_length=15)
    diaDaReserva = models.DateField(verbose_name='Dia da Reserva')
    observacoes = models.TextField(verbose_name='Observações', blank=True)

# Modelo para clientes, estendendo o modelo de usuário personalizado


class Cliente(AbstractUser):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    s_online = models.BooleanField(default=False, blank=True)
    telefone = models.CharField(max_length=15)
    telefone2 = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(
        max_length=30,
        unique=True,
        blank=True,  # Campo opcional
        null=True,
        default=None,
        validators=[UnicodeUsernameValidator()],
        help_text=("Campo de nome de usuário (opcional). "
                   "Deixe em branco para usar o email como nome de usuário.")
    )

    # Defina o campo 'username' como campo principal de autenticação
    USERNAME_FIELD = 'username'
    password = models.CharField(max_length=128, default='')  # Senha em branco

    # Resto do seu modelo aqui

    # Inclua 'email' nos REQUIRED_FIELDS
    REQUIRED_FIELDS = ['email']

    # Adicione os related_name para evitar conflitos
    groups = models.ManyToManyField(Group, related_name='clientes')
    user_permissions = models.ManyToManyField(
        Permission, related_name='clientes')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

# Modelo para categorias de animais


class CategoriaAnimal(models.Model):
    nome = models.CharField(verbose_name='Nome da Categoria', max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria de Animal'
        verbose_name_plural = 'Categorias de Animais'

# Modelo para categorias de banho


class CategoriaBanho(models.Model):
    nome = models.CharField(
        verbose_name='Nome da Categoria de Banho', max_length=50)
    preco = models.DecimalField(
        verbose_name='Preço', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria de Banho'
        verbose_name_plural = 'Categorias de Banho'
