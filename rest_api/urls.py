from django.urls import path, include
from rest_api.views import *
from rest_framework.routers import SimpleRouter
# Importe as URLs do aplicativo reserva
from reserva import urls as reserva_urls

app_name = 'rest_api'

# Criação de roteadores para as views da API
router = SimpleRouter()
router2 = SimpleRouter()

# Registra as views no roteador
router.register('agendamento', AgendamentoModelViewSet)
router2.register('contato', ContatoModelViewSet)
router.register('petshop', PetshopModelViewSet)

urlpatterns = [
    path('hello_world', hello_world, name='hello_world_api'),
    # path('contato', listar_contatos, name='listar_contatos'),
    # path('contato/<int:id>', obter_contato_pelo_id, name="obter_contato"),
    # Inclua as URLs do aplicativo reserva
    path('reserva/', include(reserva_urls, namespace='reserva')),
    path('reserva/<int:pk>/', ReservaDeBanho, name='reserva-detail')


]

# Adiciona as URLs geradas pelos roteadores às URLs da aplicação
urlpatterns += router.urls

urlpatterns += router2.urls
