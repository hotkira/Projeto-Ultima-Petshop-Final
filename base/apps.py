from django.apps import AppConfig


class BaseConfig(AppConfig):
    # Configuração para o aplicativo 'base'

    # Define o campo automático padrão para modelos como BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'

    # Nome do aplicativo
    name = 'base'

    # Nome legível para o aplicativo (aparecerá no admin)
    verbose_name = 'Módulo Geral'
