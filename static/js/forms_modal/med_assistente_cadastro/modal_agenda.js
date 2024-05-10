document.getElementById('myBtn_modal_agenda').addEventListener('click', function() {
    // Abre o modal
    console.log("carregado")
    var modal = document.getElementById("myModal_agenda");
    modal.style.display = "block";
});
// Função para fechar o modal ao clicar fora dele
function fecharModalFora(event) {
    var modal = document.getElementById("myModal_agenda");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Função para limpar os campos específicos do formulário dentro do modal
function limparCamposModal(modal) {
    // Limpa os campos específicos do modal
    modal.find('#id_data_inicio, #id_data_fim').val('');

}

// Função para emitir aviso de agenda salva e alterar o botão de acordo
function emitirAvisoAgendaSalva(btnAgenda) {
    // Emitir o aviso de agenda salva
    console.log("Agenda salva!"); // ou você pode exibir uma mensagem na interface do usuário
    
    // Alterar o texto do botão de agenda
    pAgenda.textContent = "Salva";
}

// Função para processar as mudanças nos componentes do modal
function processarMudancasModal(modal) {
    // Certifique-se de que o checkbox está checado
    modal.find('#myBtn_modal_agenda').prop('checked', true);
}

// Adicione um evento de clique para o botão de submit do modal ativo
$('#myModal_agenda').on('click', 'button[type="submit"]', function(event) {
    // Previna o comportamento padrão do botão de submit
    event.preventDefault();

    // Encontre o formulário dentro do modal atual
    var form = $(this).closest('form');

    // Teste se o formulário da agenda é válido
    if (form[0].checkValidity()) {
        // Envie o formulário via AJAX para a nova rota
        $.ajax({
            url: '/assistente/cadastro/salvar_agenda/', // Use a nova rota aqui
            method: form.attr('method'),
            data: form.serialize(),
            success: function(response) {
                // Se o formulário for válido e for salvo com sucesso, emitir aviso de agenda salva e processar mudanças no modal
                var btnAgenda = document.getElementById("myBtn_modal_agenda"); // Encontra o checkbox de agenda
                emitirAvisoAgendaSalva(btnAgenda);
                processarMudancasModal($('#myModal_agenda'));
            },
            error: function(xhr, status, error) {
                // Em caso de erro ao enviar o formulário, exiba uma mensagem de erro para o usuário
                $('#myModal_agenda').find('.modal-body').html('<div class="alert alert-danger" role="alert">Ocorreu um erro ao salvar o formulário. Por favor, tente novamente mais tarde.</div>');
            }
        });
    } else {
        // Se o formulário não for válido, exiba uma mensagem para o usuário
        $('#myModal_agenda').find('.modal-body').html('<div class="alert alert-warning" role="alert">Por favor, preencha todos os campos corretamente.</div>');
    }

    // Limpar os campos do modal
    var modal = $('#myModal_agenda');
    limparCamposModal(modal);
    // Chama a função para fechar o modal fora
    fecharModalFora();
});









// Adiciona um ouvinte de eventos para capturar os cliques fora do modal
window.addEventListener('click', fecharModalFora);