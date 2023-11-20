from django.contrib import admin
from .models import ReservaDeBanho, Petshop

# Registro do modelo ReservaDeBanho no painel de administração


@admin.register(ReservaDeBanho)
class ReservaDeBanhoAdmin(admin.ModelAdmin):
    list_display = ['get_nome_cliente', 'nomeDoPet', 'diaDaReserva',
                    'turno', 'status']
    search_fields = ['nomeDoPet']
    list_filter = ['diaDaReserva', 'turno', 'cliente__nome', 'status']

    def get_nome_cliente(self, obj):
        return obj.cliente.nome if obj.cliente else ""

    get_nome_cliente.short_description = 'Nome do Cliente'


# Registro do modelo Petshop no painel de administração


@admin.register(Petshop)
class PetshopAdmin(admin.ModelAdmin):
    list_display = ['nome', 'rua', 'numero', 'bairro']
