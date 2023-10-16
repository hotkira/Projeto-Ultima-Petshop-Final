from django.contrib import admin

from reserva.models import ReservaDeBanho

# Register your models here.
@admin.register(ReservaDeBanho)
class ReservaDeBanhoAdmin(admin.ModelAdmin):
    list_display = ['nomeDoPet', 'diaDaReserva', 'observacoes', 'turno', 'tamanho']
    search_fields = ['nomeDoPet']
    list_filter = ['diaDaReserva', 'turno', 'tamanho']
