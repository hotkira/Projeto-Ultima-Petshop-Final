from django.contrib.auth.backends import ModelBackend
from base.models import Cliente

import logging

logger = logging.getLogger(__name__)


class EmailBackend(ModelBackend):

    # Esta função autentica um usuário usando o seu usuário e senha.
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Tenta recuperar o usuário do banco de dados.
        try:
            cliente = Cliente.objects.get(username=username)
        except Cliente.DoesNotExist:
            return None

        # Registre uma mensagem de log informando que o usuário foi encontrado.
        # logger.debug(
        #     'EmailBackend: Cliente encontradocom o usuário: %s', cliente)

        # Verifique a senha do cliente.
        if cliente.check_password(password):
            return cliente

        # Se a senha estiver incorreta, retorne None.
        return None

    # Esta função recupera um usuário do banco de dados usando o seu ID.
    def get_user(self, user_id):
        # Tente recuperar o usuário do banco de dados usando o seu ID.
        try:
            return Cliente.objects.get(pk=user_id)
        except Cliente.DoesNotExist:
            return None
