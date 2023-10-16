import datetime as dt
from typing import Any

from django.core.management.base import BaseCommand
from reserva.models import ReservaDeBanho

class Command(BaseCommand):
    
    #teste: str = ''
    def add_arguments(self, parser):
        parser.add_argument('--dias', required=True, type=int)
    
    def handle(self, *args: Any, **options):
        hoje = dt.date.today()
        #usando o dias: python .\manage.py finalizar_contato --dias=2  ##quantidade de dias em numero
        dias = options['dias']
        data_base = hoje - dt.timedelta(days=7)
        reservas_antigas = ReservaDeBanho.objects.filter(diaDaReserva__lte=data_base)
        reservas_antigas.update(finalizado=True)
        # for reserva in reservas_antigas:
        #     reserva.realizado = True,
        #     reserva.save()
        