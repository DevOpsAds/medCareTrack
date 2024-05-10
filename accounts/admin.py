from django.contrib import admin
from .models import UsuarioVinculado

@admin.register(UsuarioVinculado)
class UsuarioVinculadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email',)
