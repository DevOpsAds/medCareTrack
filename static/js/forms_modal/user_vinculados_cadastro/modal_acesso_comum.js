document.getElementById('btn_cadastro_acesso_comum').addEventListener('click', function() {

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

$('#myModal_acesso_comum').on('click', 'button[type="submit"]', function(event) {
    // Previna o comportamento padrão do botão de submit
    console.log("clicqyed")
    event.preventDefault();

    // Encontre o formulário dentro do modal atual
    var form = $(this).closest('form');

    // Teste se o formulário do recurso é válido
    if (form[0].checkValidity()) {
        // Adicione manualmente o valor de usuario_principal_id ao FormData
        var formData = new FormData(form[0]);
        formData.append('usuario_principal_id', 1); // Altere para o valor desejado

        // Envie o formulário via AJAX para a nova rota
        $.ajax({
            url: '/salvar_membro_equipe/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response.success) {
                    // Redirecione para a URL especificada na resposta
                    window.location.href = response.redirect_url;
                } else {
                    // Se houver erros de validação, manipule-os aqui
                    console.error('Erros de validação:', response.errors);
                }
            },
            error: function(xhr, status, error) {
                // Manipule erros de requisição aqui, se necessário
                console.error('Erro na requisição AJAX:', error);
            }
        });
    } else {
        // Se o formulário não for válido, adicione classes de validação Bootstrap
        $('#myModal_acesso_comum').find('.modal-body').html('<div class="alert alert-warning" role="alert">Por favor, preencha todos os campos corretamente.</div>');
    }

            // Limpar os campos do modal
            var modal = $('#myModal_acesso_comum');
            limparCamposModal(modal);
            // Chama a função para fechar o modal fora
            fecharModalFora();
});







// Adiciona um ouvinte de eventos para capturar os cliques fora do modal
window.addEventListener('click', fecharModalFora);