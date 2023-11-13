import datetime as dt
from typing import Any

from django.core.management.base import BaseCommand
from reserva.models import ReservaDeBanho


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--dias', required=True, type=int,
                            help='Quantidade de dias para finalizar reservas.')

    def handle(self, *args: Any, **options):
        hoje = dt.date.today()
        dias = options['dias']
        data_base = hoje - dt.timedelta(days=dias)

        # Filtrar reservas antigas com base na data especificada
        reservas_antigas = ReservaDeBanho.objects.filter(
            diaDaReserva__lte=data_base)

        # Atualizar as reservas antigas como finalizadas
        reservas_antigas.update(finalizado=True)

        # Lógica alternativa usando um loop, se preferir
        # for reserva in reservas_antigas:
        #     reserva.finalizado = True
        #     reserva.save()

        self.stdout.write(self.style.SUCCESS(
            f'{reservas_antigas.count()} reservas foram finalizadas.'))
