from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
  help = 'Criar um token para um usuário'

  def add_arguments(self, parser):
    parser.add_argument('--usuario', required=True)
    parser.add_argument('--senha', required=True)

  def handle(self, *args, **options):
    usuario = options['usuario']
    senha = options['senha']

    self.stdout.write(
      self.style.WARNING(f'Criando usuário para user {usuario} com senha {senha}')
    )

    user = User(username=usuario)
    user.set_password(senha)
    user.save()
    
    self.stdout.write(
      self.style.WARNING('Usuário criado!')
    )

    token = Token.objects.create(user=user)

    self.stdout.write(
      self.style.WARNING(f'Token gerado: {token}')
    )

