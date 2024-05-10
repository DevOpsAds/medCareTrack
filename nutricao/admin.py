from django.contrib import admin
from .models import Alimentacao, Liquido, RegistroAlimentacao, RegistroLiquidos, EscalaQuantidade

@admin.register(Alimentacao)
class AlimentacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo_alimento', 'descricao', 'hora_consumo', 'calorias')

@admin.register(Liquido)
class LiquidoAdmin(admin.ModelAdmin):
    list_display = ('tipo_liquido', 'descricao', 'hora_consumo', 'volume_ml')

@admin.register(EscalaQuantidade)
class EscalaQuantidadeAdmin(admin.ModelAdmin):
    list_display = ('valor',)

@admin.register(RegistroAlimentacao)
class RegistroAlimentacaoAdmin(admin.ModelAdmin):
    list_display = ('user', 'horario', 'alimentacao', 'qualidade')

@admin.register(RegistroLiquidos)
class RegistroLiquidosAdmin(admin.ModelAdmin):
    list_display = ('user', 'horario', 'liquido', 'quantidade')
