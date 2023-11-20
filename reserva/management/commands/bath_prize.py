import random
from django.core.management.base import BaseCommand
from reserva.models import Petshop

# Define a classe do comando personalizado que herda da classe BaseCommand do Django.


class Command(BaseCommand):

    # Método para listar os IDs de todos os petshops no banco de dados.
    def list_petshops(self):
        petshop_ids = Petshop.objects.all().values_list('pk', flat=True)
        print('Petshop IDs:', petshop_ids)  # Adicione esta linha para depurar
        return petshop_ids

    # Método para adicionar argumentos à linha de comando.
    def add_arguments(self, parser):
        parser.add_argument(
            '--quantity',
            nargs='?',
            default=5,
            type=int,
            help='Quantas pessoas devem participar do concurso'
        )
        parser.add_argument(
            '--petshop',
            type=int,
            help='ID do Petshop para o concurso'
        )

    # Método para escolher aleatoriamente reservas de um conjunto dado.
    def escolher_reservas(self, banhos, quantidade):
        banhos_list = list(banhos)
        if quantidade > len(banhos_list):
            quantidade = len(banhos_list)
        return random.sample(banhos_list, quantidade)

    # Método principal chamado quando o comando é executado.
    def handle(self, *args, **options):
        quantity = options['quantity']
        petshop_id = options['petshop']

        # Verifica se o ID do Petshop foi fornecido
        if petshop_id is None:
            self.stdout.write(self.style.ERROR('ID do Petshop é obrigatório'))
            return

        # Agora, chame list_petshops dentro da função handle
        petshops = self.list_petshops()

        # Verifica se o ID do Petshop fornecido é válido
        if petshop_id not in petshops:
            self.stdout.write(self.style.ERROR('ID do Petshop inválido'))
            return

        # Obtém o objeto Petshop a partir do ID
        petshop = Petshop.objects.get(pk=petshop_id)
        # Obtém todas as reservas associadas ao petshop
        reservas = petshop.reservas.all()

        # Itera sobre as reservas e imprime cada uma na saída padrão.
        for reserva in reservas:
            self.stdout.write(str(reserva))

# para executar: python manage.py bath_prize  --quantity 10 --petshop 1
