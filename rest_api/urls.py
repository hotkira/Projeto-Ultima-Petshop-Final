from django.urls import path

from rest_api.views import *
from rest_framework.routers import SimpleRouter

app_name = 'rest_api'

router = SimpleRouter()
router2 = SimpleRouter()
router.register('agendamento', AgendamentoModelViewSet)
router2.register('contato', ContatoModelViewSet)
router.register('petshop', PetshopModelViewSet)

urlpatterns = [
  path('hello_world', hello_world, name='hello_world_api'),
  # path('contato', listar_contatos, name='listar_contatos'),
  # path('contato/<int:id>', obter_contato_pelo_id, name="obter_contato")
]

urlpatterns += router.urls
urlpatterns += router2.urls
