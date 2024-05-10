

document.getElementById('btn_recursos').addEventListener('click', function() {
    // Abre o modal

    var modal = document.getElementById("myModal_recurso");
    modal.style.display = "block";
});

// Função para fechar o modal ao clicar fora dele
function fecharModalFora(event) {
    var modal = document.getElementById("myModal_recurso");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Função para limpar os campos específicos do formulário dentro do modal
function limparCamposModal(modal) {
    // Limpa os campos específicos do modal
    modal.find('#id_nome, #id_tipo').val('');
    // Reseta o campo select para o valor padrão
    modal.find('select').val('').trigger('change');
}

/// Função para emitir aviso de recurso salvo e alterar o botão de acordo
function emitirAvisoRecursoSalvo(btnRecurso) {
    // Emitir o aviso de recurso salvo
    console.log("Recurso salvo!"); // ou você pode exibir uma mensagem na interface do usuário
    
    // Alterar o nome e a cor do botão de recurso
    btnRecurso.textContent = "Salvo / novo";
    btnRecurso.style.backgroundColor = "green";
}

// Adicione um evento de clique para o botão de submit do modal ativo
$('#myModal_recurso').on('click', 'button[type="submit"]', function(event) {
    // Previna o comportamento padrão do botão de submit
    event.preventDefault();

    // Encontre o formulário dentro do modal atual
    var form = $(this).closest('form');

    // Teste se o formulário do recurso é válido
    if (form[0].checkValidity()) {
        // Envie o formulário via AJAX para a nova rota
        $.ajax({
            url: '/assistente/cadastro/salvar_recurso/', // Use a nova rota aqui
            method: form.attr('method'),
            data: form.serialize(),
            success: function(response) {
                // Se o formulário for válido e for salvo com sucesso, emitir aviso de recurso salvo e alterar o botão
                var btnRecurso = document.getElementById("btn_recursos"); // Encontra o botão de recurso
                emitirAvisoRecursoSalvo(btnRecurso);
            },
            error: function(xhr, status, error) {
                // Em caso de erro ao enviar o formulário, exiba uma mensagem de erro para o usuário
                $('#myModal_recurso').find('.modal-body').html('<div class="alert alert-danger" role="alert">Ocorreu um erro ao salvar o formulário. Por favor, tente novamente mais tarde.</div>');
            }
        });
    } else {
        // Se o formulário não for válido, exiba uma mensagem para o usuário
        $('#myModal_recurso').find('.modal-body').html('<div class="alert alert-warning" role="alert">Por favor, preencha todos os campos corretamente.</div>');
    }

        // Limpar os campos do modal
        var modal = $('#myModal_recurso');
        limparCamposModal(modal);
        // Chama a função para fechar o modal fora
        fecharModalFora();
});





// Adiciona um ouvinte de eventos para capturar os cliques fora do modal
window.addEventListener('click', fecharModalFora); 