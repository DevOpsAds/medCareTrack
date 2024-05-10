# Em views.py



from django.shortcuts import render, redirect



from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from .forms import CuidadorForm,OpcoesContatoForm, AgendaDisponivelForm,RecursoDisponivelForm,CuidadorForm


from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.http import require_POST



@csrf_exempt
def salvar_recurso(request):
    if request.method == 'POST':
        # Verifica se a solicitação é AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Instancia o formulário com os dados da solicitação POST
            form = RecursoDisponivelForm(request.POST)
            # Verifica se o formulário é válido
            if form.is_valid():
                # Salva os dados do formulário
                form.save()

                # Retorna uma resposta JSON indicando sucesso
                return JsonResponse({'message': 'Recurso salvo com sucesso!'})
            else:
                # Retorna uma resposta JSON indicando erro de validação do formulário
                return JsonResponse({'error': 'Erro de validação do formulário.', 'errors': form.errors}, status=400)

    # Se a solicitação não for AJAX ou não for POST, retorne uma resposta de erro
    return JsonResponse({'error': 'Esta rota só aceita solicitações AJAX POST.'}, status=400)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import AgendaDisponivelForm  # Importe o formulário AgendaDisponivelForm

@csrf_exempt
def salvar_agenda(request):
    if request.method == 'POST':
        # Verifica se a solicitação é AJAX
        print("rota ajax 4")
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Instancia o formulário com os dados da solicitação POST
            form = AgendaDisponivelForm(request.POST)
            print(form)
            # Verifica se o formulário é válido
            if form.is_valid():
                # Salva os dados do formulário
                form.save()

                # Retorna uma resposta JSON indicando sucesso
                return JsonResponse({'message': 'Agenda disponível salva com sucesso!'})
            else:
                # Retorna uma resposta JSON indicando erro de validação do formulário
                return JsonResponse({'error': 'Erro de validação do formulário.', 'errors': form.errors}, status=400)

    # Se a solicitação não for AJAX ou não for POST, retorne uma resposta de erro
    return JsonResponse({'error': 'Esta rota só aceita solicitações AJAX POST.'}, status=400)






def cadastro(request):
    if request.method == 'POST':
        form_contato = OpcoesContatoForm(request.POST)
        form_cadastro = CuidadorForm(request.POST)
        form_agenda = AgendaDisponivelForm(request.POST)
        form_recurso = RecursoDisponivelForm(request.POST)
        form_acesso = CuidadorForm(request.POST)

        # Verificar se os formulários são válidos individualmente
        form_contato_valid = form_contato.is_valid()
        form_cadastro_valid = form_cadastro.is_valid()
        form_agenda_valid = form_agenda.is_valid()
        form_recurso_valid = form_recurso.is_valid()
        form_acesso_valid = form_acesso.is_valid()

        if form_recurso_valid:
            form_recurso.save()

        # Salvar apenas os formulários válidos
        if form_contato_valid and form_cadastro_valid:
            form_contato.save()
            form_cadastro.save()
        elif form_agenda_valid:
            form_agenda.save()

 
            # Redirecionar para uma página de sucesso ou para qualquer outra página desejada
            return redirect('pagina_sucesso')
    else:
        form_contato = OpcoesContatoForm()
        form_cadastro = CuidadorForm()
        form_agenda = AgendaDisponivelForm()
        form_recurso = RecursoDisponivelForm()
        form_acesso = CuidadorForm()
    return render(request, 'cadastro.html', {'form_contato': form_contato, 'form_cadastro': form_cadastro, 'form_agenda': form_agenda, 'form_recurso': form_recurso, 'form_acesso': form_acesso})

#**-------------