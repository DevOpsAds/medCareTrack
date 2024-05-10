from django.contrib import admin
from .models import InstrumentoAfericao, ResultadosAferitivos, Aferitivos

# Register your models here.
@admin.register(InstrumentoAfericao)
class InstrumentoAfericaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'informacoes', 'user')
    search_fields = ('nome', 'descricao')
    list_filter = ('user',)

@admin.register(ResultadosAferitivos)
class ResultadosAferitivosAdmin(admin.ModelAdmin):
    list_display = ('instrumento', 'resultados', 'resultados_anteriores')
    search_fields = ('instrumento__nome',)
    list_filter = ('instrumento',)

@admin.register(Aferitivos)
class AferitivosAdmin(admin.ModelAdmin):
    pass  # Como Aferitivos é uma classe abstrata, não precisamos de configurações adicionais para o admin
