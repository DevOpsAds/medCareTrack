document.addEventListener('DOMContentLoaded', function() {
    // Adicione um ouvinte de evento para o botão de abrir modal
    var modalBtn = document.getElementById('modalBtn_contato');
    
    // Verifica se o botão foi encontrado
    if (modalBtn) {
        console.log("Botão de abrir modal encontrado:", modalBtn);

        // Defina a função para abrir o modal
        function abrirModal() {
            // Obtém o modal
            var modal = document.getElementById("myModal");

            // Exibe o modal
            modal.style.display = "block";
        }

        // Adiciona um evento de clique ao botão
        modalBtn.addEventListener('click', function() {
            // Alerta simples ao clicar no botão
            alert("Botão de abrir modal foi clicado!");

            // Em seguida, você pode adicionar o código para carregar o conteúdo do modal e abrir o modal
            // Exemplo:
            /*
            fetch('/assistente/cadastro/contato/')
                .then(response => response.text())
                .then(data => {
                    document.getElementById('modal-content').innerHTML = data;
                    abrirModal();
                })
                .catch(error => console.error('Erro:', error));
            */
            
            // Chama a função para abrir o modal
            abrirModal();
        });
    } else {
        console.error("Botão de abrir modal não encontrado.");
    }
});
