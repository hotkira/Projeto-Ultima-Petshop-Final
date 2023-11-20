# Importando módulos e classes necessários
import datetime as dt
from typing import Any
from django.core.management.base import BaseCommand
from reserva.models import ReservaDeBanho

# Definindo uma classe de comando personalizado que herda da BaseCommand


class Command(BaseCommand):

    # Adicionando argumentos de linha de comando ao comando
    def add_arguments(self, parser):
        parser.add_argument('--dias', required=True, type=int,
                            help='Quantidade de dias para finalizar reservas.')

    # Método chamado quando o comando é executado
    def handle(self, *args: Any, **options):
        # Obtendo a data atual
        hoje = dt.date.today()

        # Obtendo o número de dias a partir dos argumentos de linha de comando
        dias = options['dias']

        # Calculando a data base subtraindo os dias especificados
        data_base = hoje - dt.timedelta(days=dias)

        # Filtrando reservas antigas com base na data especificada
        reservas_antigas = ReservaDeBanho.objects.filter(
            diaDaReserva__lte=data_base)

        # Atualizando as reservas antigas como finalizadas
        reservas_antigas.update(status="concluido")

        # Lógica alternativa usando um loop, se preferir
        # for reserva in reservas_antigas:
        #     reserva.finalizado = True
        #     reserva.save()

        # Exibindo a quantidade de reservas finalizadas no console
        self.stdout.write(self.style.SUCCESS(
            f'{reservas_antigas.count()} reservas foram finalizadas.'))


# para executar o programa: python manage.py finalizar_contato --dias=7
