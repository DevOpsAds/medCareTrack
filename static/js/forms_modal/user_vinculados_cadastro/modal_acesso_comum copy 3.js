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
    // Impedir o envio padrão do formulário
    event.preventDefault();

    // Obter o valor do campo de entrada
    var dado = document.getElementById('id_email').value;

    // Criar um objeto com os dados a serem enviados
    var dadosParaEnviar = {
        'data': dado
    };

    // Fazer uma requisição AJAX usando o método POST
    fetch('/salvar_usuario_vinculado/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Adicione o token CSRF
        },
        body: JSON.stringify(dadosParaEnviar)
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        console.log('Resposta do servidor:', data);
        // Aqui você pode fazer qualquer coisa com a resposta do servidor
    })
    .catch(function(error) {
        console.error('Ocorreu um erro:', error);
    });
});

// Função para obter o token CSRF do cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}





// Adiciona um ouvinte de eventos para capturar os cliques fora do modal
window.addEventListener('click', fecharModalFora);