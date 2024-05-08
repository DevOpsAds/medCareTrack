from django.contrib import admin
from .models import Cuidador, OpcoesContato, AgendaDisponivel, RecursoDisponivel,UsuarioCuidador

@admin.register(Cuidador)
class CuidadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade')
    filter_horizontal = ('contatos', 'agenda_disponibilidade')

@admin.register(OpcoesContato)
class OpcoesContatoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'numero_identificador')

@admin.register(AgendaDisponivel)
class AgendaDisponivelAdmin(admin.ModelAdmin):
    list_display = ('data_inicio', 'data_fim')

@admin.register(RecursoDisponivel)
class RecursoDisponivelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')


@admin.register(UsuarioCuidador)
class UsuarioCuidadorAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'cuidador']
