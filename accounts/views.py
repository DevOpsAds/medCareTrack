from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import HttpResponse
from .forms import UsuarioVinculadoForm
from django.views.decorators.csrf import csrf_exempt













from django.shortcuts import render
from django.views import View
from .forms import UsuarioVinculadoForm

class UserProfileView(View):
    def get(self, request):
        print("aqui 2 novo")
        # Obtenha o ID do usuário atualmente logado
        user_id = request.user.id

        # Instancie o formulário com o ID do usuário como um dicionário de dados iniciais
        form = UsuarioVinculadoForm(initial={'usuario_principal_id': user_id})

        # Renderize o template pai e inclua o modal com o formulário
        return render(request, 'profile.html', {'form': form, 'user_id': user_id})
       

def criar_usuario_vinculado(request, form):
    # Obtenha o ID do usuário atualmente logado
    user_id = request.user.id

    # Renderize o formulário no contexto do template modal
    return render(request, 'modal/modal_acesso_userVinculado.html', {'form': form, 'user_id': user_id})



@csrf_exempt
def salvar_usuario_vinculado(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        print('veio ')
        print(request.POST)  # Se for uma requisição POST com formulário de dados
        form = UsuarioVinculadoForm(request.POST, user=request.user)
        if form.is_valid():
            usuario_vinculado = form.save()
            return JsonResponse({'success': True, 'redirect_url': '/accounts/profile'})
        else:
            # Se o formulário não for válido, retorne uma resposta indicando os erros
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})

    # Se a solicitação não for AJAX, retorne um erro 400 (Bad Request)
    return JsonResponse({'error': 'Requisição inválida'}, status=400)
#---------------------bom
def salvassr_usuario_vinculado(request):
    if request.method == 'POST':
        # Verifica se a solicitação é AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                print('veio ')
                print(request.POST)  # Se for uma requisição POST com formulário de dados
                form = UsuarioVinculadoForm(request.POST, user=request.user)
                print(form)
                if form.is_valid():
                    usuario_vinculado = form.save()
                    return redirect('//account/prodfile')
        # Faça o processamento dos dados aqui

        # Retorne uma resposta adequada para o AJAX
        return JsonResponse({'message': 'Dados recebidos e processados com sucesso!'})

    # Se a requisição não for POST, retorne algo (pode ser vazio neste caso)
    return JsonResponse({'message': 'Requisição deve ser do tipo POST.'})

    # Se a solicitação não for AJAX ou não for POST, retorne uma resposta de erro
    return JsonResponse({'error': 'Esta rota só aceita solicitações AJAX POST.'}, status=400)


#________________________________________________________________


def salvddar_usuario_vinculado(request):
    if request.method == 'POST':
        # Aqui você pode acessar os dados enviados pelo AJAX
        # Por exemplo, se estiver esperando um JSON, pode acessá-lo assim:
        data = request.POST.get('data')  # Supondo que você esteja enviando 'data' no seu AJAX
        print(request.POST)  # Se for uma requisição POST com formulário de dados
        # Faça o processamento dos dados aqui

        # Retorne uma resposta adequada para o AJAX
        return JsonResponse({'message': 'Dados recebidos e processados com sucesso!'})

    # Se a requisição não for POST, retorne algo (pode ser vazio neste caso)
    return JsonResponse({'message': 'Requisição deve ser do tipo POST.'})


@csrf_exempt
def sddalvar_usuario_vinculado(request):
    if request.method == 'POST':

        print('AJax')
        print(request.POST)  # Se for uma requisição POST com formulário de dados
            # Ou
        print(request.body)  # Se for uma requisição POST com dados em formato JSON
# Verifica se a solicitação é AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Instancia o formulário com os dados da solicitação POST e o usuário atual
            form = UsuarioVinculadoForm(request.POST, user=request.user)
            
            # Verifica se o formulário é válido
            if form.is_valid():
                # Salva os dados do formulário
                form.save()

                # Retorna uma resposta JSON indicando sucesso
                return JsonResponse({'message': 'Recurso salvo com sucesso!'})
            else:
                # Retorna uma resposta JSON indicando erro de validação
                return JsonResponse({'errors': form.errors}, status=400)
    # Se a solicitação não for AJAX ou não for POST, retorne uma resposta de erro
    return JsonResponse({'error': 'Esta e um bosta rota só aceita solicitações AJAX POST.'}, status=410)




#=================================

#_____________________________________



class UsersProfileView(View):
    def get(self, request):
        print("aqui 2 novo")
        # Obtenha o ID do usuário atualmente logado
        user_id = request.user.id

        # Instancie o formulário com o ID do usuário como um dicionário de dados iniciais
        form = UsuarioVinculadoForm(initial={'usuario_principal_id': user_id})
        criar_usuario_vinculado(request,form)
        # Renderize o template pai e inclua o modal com o formulário
        return render(request, 'profile.html' )
       

def criar_usuario_vinculado(request,form):
        form=form
        # Renderize o formulário no contexto do template
        return render(request, 'modal/modal_acesso_userVinculado.html', {'form': form, 'user_id': user_id})



def crisar_ussuario_vinculado(request):
    print('aqui 33')
    if request.method == 'POST':
        print('314')
        print(request.POST)  # Se for uma requisição POST com formulário de dados
            # Ou
        print(request.body)  # Se for uma requisição POST com dados em formato JSON

        form = UsuarioVinculadoForm(request.POST, user=request.user)
        if form.is_valid():
            usuario_vinculado = form.save()
            return redirect('account/profile')  # Redireciona para uma view chamada 'sucesso'
    else:
        form = UsuarioVinculadoForm()

    return render(request, 'modal/modal_acesso_userVinculado.html', {'form': form})


class UsserProfileView(View):
    def get(self, request):
        criar_usuario_vinculado(request)
        print("aqui2")
        # Obtenha o usuário atualmente logado
        user = request.user
        print(user)
        # Obtenha a chave primária (PK) do usuário logado
        user_pk = user.id
        print(user_pk)
        form_us_vinc = UsuarioVinculadoForm()
        # Renderize o template do perfil do usuário com os dados do usuário e sua PK
        return render(request, 'profile.html', {'user': user, 'user_pk': user_pk, 'form_us_vinc': form_us_vinc})

    def post(self, request):
        print("55")
        # Criar uma instância do formulário com os dados recebidos na requisição
        form_us_vinc = UsuarioVinculadoForm(request.POST)
        # Verificar se o formulário é válido
        if form_us_vinc.is_valid():
            # Se válido, salvar os dados do formulário e associar ao usuário
            usuario_vinculado = form_us_vinc.save(commit=False)
            usuario_vinculado.usuario = request.user
            usuario_vinculado.save()
            # Redirecionar para algum lugar, talvez a página de perfil novamente
            return redirect('profile')  # Lembre-se de substituir 'profile' pelo nome correto da sua view de perfil
        else:
            # Se o formulário não for válido, re-renderizar o template com os erros
            return render(request, 'profile.html', {'form_us_vinc': form_us_vinc})






@login_required
def profiled(request):
    criar_usuario_vinculado(request)
    user = request.user  # Acessa o usuário logado
    print("aqui1")
    context = {
        'user': user
    }

    return render(request, 'profile.html', context)






def criar_ussuario_vinculado(request):
    if request.method == 'POST':
        print("aqui3")
        form_us_vinc = UsuarioVinculadoForm(request.POST)
    else:
        form_us_vinc = UsuarioVinculadoForm()
    return render(request, 'modal/modal_acesso_userVinculado.html', {'form_us_vinc': form_us_vinc})



@login_required
def admin_only_view(request):
    if not request.user.is_staff:
        return HttpResponse("Você não tem permissão para acessar esta página.")
    # Implemente o código que deseja executar para usuários administradores
    return HttpResponse("Esta é uma visualização restrita para administradores.")



from django.http import JsonResponse
from .forms import UsuarioVinculadoForm

from django.http import JsonResponse
from .forms import UsuarioVinculadoForm

#=================================
@csrf_exempt
def salvar_uddsuario_vinculado(request):
    if request.method == 'POST':
        # Verifica se a solicitação é AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Instancia o formulário com os dados da solicitação POST
            form = UsuarioVinculadoForm(request.POST)
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
    return JsonResponse({'error': 'Esta e um bosta rota só aceita solicitações AJAX POST.'}, status=410)





def salvar_usuario_vinculado31(request):
    if request.method == 'POST':
         if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            print(request.POST)  # Se for uma requisição POST com formulário de dados
            # Ou
            print(request.body)  # Se for uma requisição POST com dados em formato JSON

            form = UsuarioVinculadoForm(request.POST)
            if form.is_valid():
                print("formulario e valido")
                usuario_principal_id = request.POST.get('usuario_principal_id')
                usuario_principal = User.objects.get(pk=usuario_principal_id)
                usuario_vinculado = form.save(commit=False)
                usuario_vinculado.usuario_principal = usuario_principal  # Atribui o objeto User
                usuario_vinculado.save()
                nome_usuario = usuario_vinculado.nome
                return JsonResponse({'message': 'Usuário vinculado salvo com sucesso!', 'nome_usuario': nome_usuario})
            else:
                return JsonResponse({'error': 'Erro de validação do formulário.', 'errors': form.errors}, status=410)

    return JsonResponse({'error': 'Esta rota só aceita solicitações AJAX POST.'}, status=411)

from django.contrib.auth.models import User

def dfsalvar_usuario_vinculado(request):
    if request.method == 'POST':
        if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = UsuarioVinculadoForm(request.POST)
            if form.is_valid():
                usuario_principal_id = request.POST.get('usuario_principal_id')
                usuario_principal = User.objects.get(pk=usuario_principal_id)
                usuario_vinculado = form.save(commit=False)
                usuario_vinculado.usuario_principal = usuario_principal
                usuario_vinculado.save()
                nome_usuario = usuario_vinculado.nome
                return JsonResponse({'message': 'Usuário vinculado salvo com sucesso!', 'nome_usuario': nome_usuario})
    
    return JsonResponse({'error': 'Esta rota só aceita solicitações AJAX POST.'}, status=400)



def atest_usuario_vinculado(request):
    if request.method == 'POST':
        print(request.POST)  # Se for uma requisição POST com formulário de dados
            # Ou
        print(request.body)  # Se for uma requisição POST com dados em formato JSON

        form = UsuarioVinculadoForm(request.POST, user=request.user)  # Passe o usuário logado para o formulário
        if form.is_valid():
            usuario_vinculado = form.save()
            nome_usuario = usuario_vinculado.nome
            return JsonResponse({'message': 'Usuário vinculado salvo com sucesso!', 'nome_usuario': nome_usuario})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'error': errors}, status=400)

    form = UsuarioVinculadoForm()  # Crie uma instância do formulário vazio
    return render(request, 'testeform.html', {'form': form})

def test_usuario_vinculado(request):
    if request.method == 'POST':
        print(request.POST)  # Se for uma requisição POST com formulário de dados
            # Ou
        print(request.body)  # Se for uma requisição POST com dados em formato JSON

        form = UsuarioVinculadoForm(request.POST, user=request.user)
        if form.is_valid():
            usuario_vinculado = form.save()
            return redirect('account/profile')  # Redireciona para uma view chamada 'sucesso'
    else:
        form = UsuarioVinculadoForm()

    return render(request, 'testeform.html', {'form': form})
