from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from base.views import inicio, contato, reservaDeBanho, cadastrar_cliente, register, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastrar-cliente', cadastrar_cliente, name='cadastrar-cliente'),
    path('contato/', contato),
    path('reserva-de-banho', reservaDeBanho, name='reservaDeBanho'),
    path('reserva/', include('reserva.urls', namespace='reserva')),
    path('api/', include('rest_api.urls', namespace='api'))
]
