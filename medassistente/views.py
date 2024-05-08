# Em views.py



from django.shortcuts import render, redirect



from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from .forms import CuidadorForm,OpcoesContatoForm, AgendaDisponivelForm,RecursoDisponivelForm,UsuarioCuidadorForm


from django.contrib.auth import views as auth_views


def cadastro(request):
    if request.method == 'POST':
        form_contato = OpcoesContatoForm(request.POST)
        form_cadastro = CuidadorForm(request.POST)
        form_agenda = AgendaDisponivelForm(request.POST)
        form_recurso = RecursoDisponivelForm(request.POST)
        form_acesso = UsuarioCuidadorForm(request.POST)

        # Verificar se os formulários são válidos individualmente
        form_contato_valid = form_contato.is_valid()
        form_cadastro_valid = form_cadastro.is_valid()
        form_agenda_valid = form_agenda.is_valid()
        form_recurso_valid = form_recurso.is_valid()
        form_acesso_valid = form_acesso.is_valid()

        # Salvar apenas os formulários válidos
        if form_contato_valid and form_cadastro_valid:
            form_contato.save()
            form_cadastro.save()
        elif form_agenda_valid:
            form_agenda.save()
        elif form_recurso_valid:
            form_recurso.save()
        elif form_acesso_valid:
            form_acesso.save()
 
            # Redirecionar para uma página de sucesso ou para qualquer outra página desejada
            return redirect('pagina_sucesso')
    else:
        form_contato = OpcoesContatoForm()
        form_cadastro = CuidadorForm()
        form_agenda = AgendaDisponivelForm()
        form_recurso = RecursoDisponivelForm()
        form_acesso = UsuarioCuidadorForm()
    return render(request, 'cadastro.html', {'form_contato': form_contato, 'form_cadastro': form_cadastro, 'form_agenda': form_agenda, 'form_recurso': form_recurso, 'form_acesso': form_acesso})

#**-------------