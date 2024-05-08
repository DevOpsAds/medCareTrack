# Em farmacia/urls.py
from django.contrib.admin.views.decorators import staff_member_required


from django.urls import path
from .views import listar_medicamentos, entrada_estoque ,detalhe_medicamento, modal_estoque



urlpatterns = [
    # Outras URLs do seu aplicativo
    path('entrada-estoque/<int:medicamento_id>/', staff_member_required(entrada_estoque), name='entrada_estoque'),
    path('listar_medicamentos/', listar_medicamentos, name='listar_medicamentos'),
    path('medicamento/detalhe/<int:medicamento_id>/', detalhe_medicamento, name='detalhe_medicamento'),
    #path('estoque/modal/<int:medicamento_id>/', modal_estoque, name='modal_estoque'),
]
