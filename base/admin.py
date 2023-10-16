from django.contrib import admin
from django.contrib import messages

from base.models import Contato

@admin.action(description='Marcar formulários de contatos selecionados com lido')
def marcar_como_lido(modeladmin, request, queryset):
  queryset.update(lido=True)
  modeladmin.message_user(request, 'Os formulários de contatos foram marcados como lido!', messages.SUCCESS)


@admin.action(description='Marcar formulários de contatos selecionados com não lido')
def marcar_como_nao_lido(modeladmin, request, queryset):
  queryset.update(lido=False)
  modeladmin.message_user(request, 'Os formulários de contatos foram marcados como não lido!', messages.SUCCESS)


# Register your models here.
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'email', 'mensagem', 'data', 'lido']
  search_fields = ['nome', 'email']
  list_filter = ['data', 'lido']
  actions = [marcar_como_lido, marcar_como_nao_lido]
