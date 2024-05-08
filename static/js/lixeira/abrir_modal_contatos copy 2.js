document.addEventListener('DOMContentLoaded', function() {
    // Adicione um ouvinte de evento para o botão de abrir modal
    var modalBtn = document.getElementById('modalBtn_contato');

    // Defina a função para abrir o modal
    function abrirModal() {
        // Obtém o modal
        var modal = document.getElementById("myModal");
        console.log("function lida")
        // Exibe o modal
        modal.style.display = "block";
    }

    modalBtn.addEventListener('click', function() {
        // Em seguida, você pode adicionar o código para carregar o conteúdo do modal e abrir o modal
        // Aqui você pode fazer uma requisição para carregar o conteúdo do formulário de contato
        console.log("chamada efetuad")
        fetch('/assistente/cadastro/contato/')
            .then(response => response.text())
            .then(data => {
                // Atualiza o conteúdo do modal com o conteúdo do formulário de contato
                document.getElementById('modal-content').innerHTML = data;
                // Abre o modal
                abrirModal();
            })
            .catch(error => console.error('Erro:', error));
    });
});
