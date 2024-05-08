document.addEventListener('DOMContentLoaded', function() {
    // Adicione um ouvinte de evento para o botão de abrir modal
    var modalBtn = document.getElementById('modalBtn_contato');
     console.log ("------------ddf----------------");
     alert("Botão de abrir modal foi clicado!",modalBtn);
    // Defina a função para abrir o modal

    modalBtn.addEventListener('click', function() {
        // Alerta simples ao clicar no botão
        //alert("Botão de abrir modal foi clicado!");
        
        // Em seguida, você pode adicionar o código para carregar o conteúdo do modal e abrir o modal
        // Exemplo:
         fetch('/assistente/cadastro/contato/')
            .then(response => response.text())
            .then(data => {
               document.getElementById('modal-content').innerHTML = data;
                abrirModal();
            })
            .catch(error => console.error('Erro:', error));

        
    });

    function abrirModal() {
        // Obtém o modal
        var modal = document.getElementById("myModal");
        console.log("Abertura simplificada")
    
        // Exibe o modal
        modal.style.display = "block";
        }
});
