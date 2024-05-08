from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    user = request.user  # Acessa o usuário logado

    context = {
        'user': user
    }

    return render(request, 'profile.html', context)

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def admin_only_view(request):
    if not request.user.is_staff:
        return HttpResponse("Você não tem permissão para acessar esta página.")
    # Implemente o código que deseja executar para usuários administradores
    return HttpResponse("Esta é uma visualização restrita para administradores.")
