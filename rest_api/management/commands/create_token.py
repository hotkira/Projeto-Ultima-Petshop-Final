from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = 'Criar um token para um usuário'

    def add_arguments(self, parser):
        # Define argumentos de linha de comando para o nome de usuário e senha
        parser.add_argument('--usuario', required=True)
        parser.add_argument('--senha', required=True)

    def handle(self, *args, **options):
        # Obtém os valores dos argumentos da linha de comando
        usuario = options['usuario']
        senha = options['senha']

        # Exibe uma mensagem informando a criação do usuário
        self.stdout.write(
            self.style.WARNING(
                f'Criando usuário para user {usuario} com senha {senha}')
        )

        # Cria um novo usuário com o nome de usuário especificado
        # ex: python manage.py create_token --usuario teste1 --senha teste1
        user = User(username=usuario)
        user.set_password(senha)
        user.save()

        # Exibe uma mensagem informando que o usuário foi criado
        self.stdout.write(
            self.style.WARNING('Usuário criado!')
        )

        # Cria um token de autenticação para o usuário
        token = Token.objects.create(user=user)

        # Exibe o token gerado
        self.stdout.write(
            self.style.WARNING(f'Token gerado: {token}')
        )
