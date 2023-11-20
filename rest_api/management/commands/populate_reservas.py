from django.core.management.base import BaseCommand
from model_bakery import baker
from reserva.models import ReservaDeBanho, Petshop, CategoriaAnimal, CategoriaBanho
from base.models import Cliente


class Command(BaseCommand):
    help = 'Criar reservas fakes para a nossa aplicação'

    def handle(self, *args, **options):
        quantidadeTotal = 100

        self.stdout.write(
            self.style.WARNING(f'Gerando {quantidadeTotal} reservas fakes')
        )

        # Criando instâncias de modelos relacionados para serem usadas nas reservas fictícias
        # com nomes mais curtos
        cliente = baker.make(Cliente, nome='Cliente Curto')
        petshop = baker.make(Petshop, nome='Petshop Curto')
        categoria_animal = baker.make(CategoriaAnimal, nome='Categoria Curta')
        categoria_banho = baker.make(CategoriaBanho, nome='Banho Curto')

        for i in range(quantidadeTotal):
            # Criando uma reserva fictícia
            reserva = baker.make(
                ReservaDeBanho,
                cliente=cliente,  # Atribuindo um cliente específico à reserva
                petshop=petshop,  # Atribuindo um petshop específico à reserva
                # Atribuindo uma categoria de animal específica à reserva
                categoriaAnimal=categoria_animal,
                # Atribuindo uma categoria de banho específica à reserva
                categoriaBanho=categoria_banho
            )

            reserva.save()

            self.stdout.write(
                self.style.WARNING(f'Criada a reserva de número {i + 1}')
            )

        self.stdout.write(
            self.style.SUCCESS('Reservas criadas com sucesso!')
        )

# para executar o proograma: python manage.py populate_reservas
