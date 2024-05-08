document.addEventListener('DOMContentLoaded', function() {
    // Adicione um ouvinte de evento para o botão de abrir modal
    var modalBtn = document.getElementById('modalBtn_contato');

    // Defina a função para abrir o modal
    function abrirModal() {
        // Obtém o modal
        console.log("chegou aqui!")
       // Obtém o botão que abre o modal
            var btn = document.getElementById("modalBtn_contato");



            // Quando o usuário clica no botão, abre o modal
            btn.onclick = function() {
                fetch('/assistente/cadastro/contato/')
                .then(response => response.text())
                .then(data => {
                document.getElementById('modal-content').innerHTML = data;
                abrirModal();
            })
            .catch(error => console.error('Erro:', error));
                console.log("abrindo modal block")
                var modal = document.getElementById("myModal");
                modal.style.display = "block";
            }


    }

    modalBtn.addEventListener('click', function() {
        // Em seguida, você pode adicionar o código para carregar o conteúdo do modal e abrir o modal
        // Aqui você pode fazer uma requisição para carregar o conteúdo do formulário de contato
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
