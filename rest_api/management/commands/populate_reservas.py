from django.core.management.base import BaseCommand
from model_bakery import baker

from reserva.models import ReservaDeBanho

class Command(BaseCommand):
  help = 'Criar reservas fakes para a nossa aplicação'

  def handle(self, *args, **options):
    quantidadeTotal = 100

    self.stdout.write(
      self.style.WARNING(f'Gerando {quantidadeTotal} reservas fakes')
    )

    for i in range(quantidadeTotal):
      reserva = baker.make(ReservaDeBanho)
      reserva.save()
      self.stdout.write(
        self.style.WARNING(f'Criada a reserva de número {i + 1}')
      )


    self.stdout.write(
      self.style.SUCCESS('Reservas criadas com sucesso!')
    )