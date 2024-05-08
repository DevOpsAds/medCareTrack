from django.contrib import admin
from .models import Medicamento, MedicamentoExtendido, Estoque,MovimentoEstoque

# Register your models here.
admin.site.register(Medicamento)
admin.site.register(MedicamentoExtendido)
admin.site.register(Estoque)
admin.site.register(MovimentoEstoque)
