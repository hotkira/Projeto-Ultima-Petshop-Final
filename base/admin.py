from django.contrib import admin, messages
from .models import Contato, Cliente, CategoriaAnimal, CategoriaBanho, User


# Personalize o nome do aplicativo
admin.site.site_header = 'Petshop Ultima Admin'


@admin.action(description='Marcar formulários de contatos selecionados como lidos')
def marcar_como_lido(modeladmin, request, queryset):
    """Ação para marcar formulários de contatos selecionados como lidos."""
    queryset.update(lido=True)
    modeladmin.message_user(
        request, 'Os formulários de contatos foram marcados como lidos!', messages.SUCCESS)

# Ação para marcar formulários de contatos selecionados como não lidos


@admin.action(description='Marcar formulários de contatos selecionados como não lidos')
def marcar_como_nao_lido(modeladmin, request, queryset):
    """Ação para marcar formulários de contatos selecionados como não lidos."""
    queryset.update(lido=False)
    modeladmin.message_user(
        request, 'Os formulários de contatos foram marcados como não lidos!', messages.SUCCESS)


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    """Administração de Contatos."""
    list_display = ['nome', 'email', 'data', 'lido', 'finalizado']
    search_fields = ['nome', 'email']
    list_filter = ['data', 'lido']
    actions = [marcar_como_lido, marcar_como_nao_lido]


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """Administração de Clientes."""
    list_display = ('nome', 'cpf', 'email', 'endereco',
                    'telefone', 'telefone2')

    # Personalize o nome exibido no painel de administração
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cliente cadastrado'
        verbose_name_plural = 'Clientes cadastrados'


@admin.register(CategoriaAnimal)
class CategoriaAnimalAdmin(admin.ModelAdmin):
    """Administração de Categorias de Animais."""
    list_display = ['nome']


@admin.register(CategoriaBanho)
class CategoriaBanhoAdmin(admin.ModelAdmin):
    """Administração de Categorias de Banho."""
    list_display = ['nome', 'preco']


# admin.site.register(User)
