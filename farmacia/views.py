# Em views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamento, Estoque, MovimentoEstoque,MedicamentoExtendido
from .forms import EntradaEstoqueForm


from django.shortcuts import render, get_object_or_404
from .models import Medicamento


from django.http import JsonResponse
from .models import MedicamentoExtendido

def modal_estoque(request, medicamento_id):
    estoque = Estoque.objects.get(medicamento_id=medicamento_id)
    return estoque

def detalhe_medicamento(request, medicamento_id):
    try:
        medicamento = get_object_or_404(MedicamentoExtendido, medicamento_id=medicamento_id)
        estoque = modal_estoque(request, medicamento_id)  # Chamando a função modal_estoque aqui
        return render(request, 'detalhe_medicamento.html', {'medicamento': medicamento, 'estoque': estoque})
    except MedicamentoExtendido.DoesNotExist:
        return JsonResponse({'error': 'Medicamento não encontrado'}, status=404)



def listar_medicamentos(request):
    
    # Obter todos os medicamentos do banco de dados
    medicamentos = Medicamento.objects.all()
    # Renderizar o template com a lista de medicamentos
    return render(request, 'listar_medicamentos.html', {'medicamentos': medicamentos})




def entrada_estoque(request, medicamento_id):
    
    medicamento = Medicamento.objects.get(pk=medicamento_id)
    if request.method == 'POST':
        form = EntradaEstoqueForm(request.POST)
        if form.is_valid():
            quantidade_entrada = form.cleaned_data['quantidade']
            estoque, created = Estoque.objects.get_or_create(medicamento=medicamento)
            estoque.quantidade_atual += quantidade_entrada
            estoque.save()
            movimento = MovimentoEstoque.objects.create(medicamento=medicamento, quantidade=quantidade_entrada, usuario=request.user)
            return redirect('detalhes_medicamento', medicamento_id=medicamento_id)
    else:
        form = EntradaEstoqueForm()
    return render(request, 'entrada_estoque.html', {'form': form, 'medicamento': medicamento})




