// Arquivo para controlar as funcionalidades do modal



// Função para fechar o modal ao clicar fora dele
function fecharModalFora(event) {
    var modal = document.getElementById("myModal_acesso");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Adiciona um ouvinte de eventos para capturar os cliques fora do modal
window.addEventListener('click', fecharModalFora);
