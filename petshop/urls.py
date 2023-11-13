from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from base.views import inicio, contato, reservaDeBanho, cadastrar_cliente, register, login_view

urlpatterns = [
    # URL para a área de administração do Django
    path('admin/', admin.site.urls),

    # URL da página inicial do site
    path('', inicio, name='inicio'),

    # URLs relacionadas à autenticação
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),

    # URL para cadastrar cliente
    path('cadastrar-cliente', cadastrar_cliente, name='cadastrar-cliente'),


    # URL para a página de contato
    path('contato/', contato, name='contato'),


    # URL para a reserva de banho
    path('reserva-de-banho', reservaDeBanho, name='reservaDeBanho'),

    # Inclui URLs do aplicativo 'reserva' com o namespace 'reserva'
    path('reserva/', include('reserva.urls', namespace='reserva')),

    # Inclui URLs do aplicativo 'rest_api' com o namespace 'api'
    path('api/', include('rest_api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls')),
]
