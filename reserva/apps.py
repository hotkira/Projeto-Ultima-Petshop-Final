from django.apps import AppConfig


class ReservaConfig(AppConfig):
    # Configuração para o aplicativo "reserva"

    # Define o campo automático padrão para modelos como BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'

    # Nome do aplicativo
    name = 'reserva'
