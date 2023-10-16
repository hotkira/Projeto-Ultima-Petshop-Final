from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Contato(models.Model):
  nome = models.CharField(max_length=50)
  email = models.EmailField(max_length=75)
  mensagem = models.TextField()
  data = models.DateTimeField(auto_now_add=True)
  lido = models.BooleanField(default=False, blank=True)
  #feito para testar os comandos do django
  finalizado = models.BooleanField(verbose_name='Finalizado', default=False, blank=True)

  def __str__(self):
    return f'Nome: {self.nome} - Email: {self.email}'
  class Meta:
    verbose_name = 'Formulário de Contato'
    verbose_name_plural = 'Formulários de Contatos'
    ordering = ['-nome']


class ReservaDeBanhoBase(models.Model):
  nomeDoPet = models.CharField(verbose_name='Nome do PET', max_length=50)
  telefone = models.CharField(verbose_name='Telefone', max_length=15)
  diaDaReserva = models.DateField(verbose_name='Dia da Reserva')
  observacoes = models.TextField(verbose_name='Observações', blank=True)


#antigo Cliente  
class Cliente(AbstractUser):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    telefone2 = models.CharField(max_length=15, blank=True, null=True)

    # Adicione related_names personalizados para evitar conflitos
    groups = models.ManyToManyField(Group, blank=True, related_name='Cliente_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='Cliente_set')

    def __str__(self):
        return self.nome
      
      

class CategoriaAnimal(models.Model):
    nome = models.CharField(verbose_name='Nome da Categoria', max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria de Animal'
        verbose_name_plural = 'Categorias de Animais'

class RacaAnimal(models.Model):
    raca = models.CharField(verbose_name='Raça do Animal', max_length=50)

    def __str__(self):
        return self.raca

    class Meta:
        verbose_name = 'Raça do Animal'
        verbose_name_plural = 'Raças dos Animais'


        
class CategoriaBanho(models.Model):
    nome = models.CharField(verbose_name='Nome da Categoria de Banho', max_length=50)
    preco = models.DecimalField(verbose_name='Preço', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria de Banho'
        verbose_name_plural = 'Categorias de Banho'



