from django.core.management.base import BaseCommand
from model_bakery import baker
from reserva.models import ReservaDeBanho


class Command(BaseCommand):
    help = 'Criar reservas fakes para a nossa aplicação'

    def handle(self, *args, **options):
        quantidadeTotal = 100

        # Exibe uma mensagem informando a geração das reservas fictícias
        self.stdout.write(
            self.style.WARNING(f'Gerando {quantidadeTotal} reservas fakes')
        )

        # Loop para criar as reservas fictícias
        for i in range(quantidadeTotal):
            reserva = baker.make(ReservaDeBanho)  # Cria uma reserva fictícia
            reserva.save()  # Salva a reserva no banco de dados (opcional)
            self.stdout.write(
                self.style.WARNING(f'Criada a reserva de número {i + 1}')
            )

        # Exibe uma mensagem informando que as reservas foram criadas com sucesso
        self.stdout.write(
            self.style.SUCCESS('Reservas criadas com sucesso!')
        )
