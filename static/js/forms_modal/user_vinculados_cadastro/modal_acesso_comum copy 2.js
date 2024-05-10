document.getElementById('btn_cadastro_acesso_comum').addEventListener('click', function() {
    // Abre o modal
    console.log("carregado")
    var modal = document.getElementById("myModal_acesso_comum");
    modal.style.display = "block";
});

// Função para fechar o modal ao clicar fora dele
function fecharModalFora(event) {
    var modal = document.getElementById("myModal_acesso_comum");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Função para limpar os campos específicos do formulário dentro do modal
function limparCamposModal(modal) {
    // Limpa os campos específicos do modal
    modal.find('#id_nome, #id_email, #id_senha').val('');
}

/// Função para emitir aviso de recurso salvo e alterar o botão de acordo
function emitirAvisoRecursoSalvo(btnRecurso, nomeUsuario) {
    // Emitir o aviso de recurso salvo
    alert("Usuário cadastrado com sucesso!");
    console.log("Usuário salvo: " + nomeUsuario); // ou você pode exibir uma mensagem na interface do usuário
    
    // Alterar o nome e a cor do botão de recurso
    btnRecurso.textContent = "Salvo / Novo";
    btnRecurso.style.backgroundColor = "green";

    // Exibir o nome do usuário cadastrado
    document.getElementById("nome").textContent = nomeUsuario;
}

// Adicione um evento de clique para o botão de submit do modal ativo
$('#myModal_acesso_comum').on('click', 'button[type="submit"]', function(event) {
    // Previna o comportamento padrão do botão de submit
    event.preventDefault();

      
    var form = document.getElementById("myForm");
    var formData = new FormData(form);
    
    // Adicione o user_id aos dados do formulário
    var user_id =  document.getElementById('user_id').value;
   
    console.log("PPPPPPPPPPPPPPPPPP",user_id);
    // Encontre o formulário dentro do modal atual
    var form = $(this).closest('form');

    // Teste se o formulário do usuário vinculado é válido
    if (form[0].checkValidity()) {
        // Obter a chave primária (PK) do usuário logado do atributo de dados do formulário
       
        // Envie o formulário via AJAX para a nova rota
        $.ajax({
            url: '/salvar_membro_equipe/', // Altere para a rota que lida com o salvamento do usuário vinculado
            method: form.attr('method'), 
            data: {
                'nome': $('#id_nome').val(),
                'email': $('#id_email').val(),
                'senha': $('#id_senha').val(),
                'usuario_principal_id':user_id, // Adicione a chave primária (PK) do usuário logado aos dados enviados
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val() // Adicione o token CSRF
            },
            
            success: function(response) {
                // Se o formulário for válido e for salvo com sucesso, emitir aviso de recurso salvo e alterar o botão
                var btnUsuarioVinculado = document.getElementById("btn_usuario_vinculado"); // Encontra o botão de usuário vinculado
                emitirAvisoRecursoSalvo(btnUsuarioVinculado);
            },
            error: function(xhr, status, error) {
                // Em caso de erro ao enviar o formulário, exiba uma mensagem de erro para o usuário
                $('#myModal_usuario_vinculado').find('.modal-body').html('<div class="alert alert-danger" role="alert">Ocorreu um erro ao salvar o formulário. Por favor, tente novamente mais tarde.</div>');
            }
        });
    } else {
        // Se o formulário não for válido, exiba uma mensagem para o usuário
        $('#myModal_usuario_vinculado').find('.modal-body').html('<div class="alert alert-warning" role="alert">Por favor, preencha todos os campos corretamente.</div>');
    }
});




// Adiciona um ouvinte de eventos para capturar os cliques fora do modal
window.addEventListener('click', fecharModalFora);