import random
from django.core.management.base import BaseCommand
from reserva.models import Petshop


class Command(BaseCommand):
    def list_petshops(self):
        petshop_ids = Petshop.objects.all().values_list('pk', flat=True)
        print('Petshop IDs:', petshop_ids)  # Adicione esta linha para depurar
        return petshop_ids

    def add_arguments(self, parser):
        parser.add_argument(
            '--quantity',  # Alterado para opção com dois traços
            nargs='?',
            default=5,
            type=int,
            help='Quantas pessoas devem participar do concurso'
        )
        parser.add_argument(
            '--petshop',  # Alterado para opção com dois traços
            type=int,
            help='ID do Petshop para o concurso'
        )

    def escolher_reservas(self, banhos, quantidade):
        banhos_list = list(banhos)
        if quantidade > len(banhos_list):
            quantidade = len(banhos_list)
        return random.sample(banhos_list, quantidade)

    def handle(self, *args, **options):
        quantity = options['quantity']
        petshop_id = options['petshop']

        # Verifique se o ID do Petshop foi fornecido
        if petshop_id is None:
            self.stdout.write(self.style.ERROR('ID do Petshop é obrigatório'))
            return

        # Agora, chame list_petshops dentro da função handle
        petshops = self.list_petshops()

        if petshop_id not in petshops:
            self.stdout.write(self.style.ERROR('ID do Petshop inválido'))
            return

        petshop = Petshop.objects.get(pk=petshop_id)
        reservas = petshop.reservas.all()

        for reserva in reservas:
            self.stdout.write(str(reserva))
