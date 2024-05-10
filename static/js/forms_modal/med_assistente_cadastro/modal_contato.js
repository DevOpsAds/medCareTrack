document.getElementById('modalBtn_contato').addEventListener('click', function() {
    // Abre o modal
    var modal = document.getElementById("myModal_contato");
    modal.style.display = "block";
});

// Função para fechar o modal ao clicar fora dele
function fecharModalFora(event) {
    var modal = document.getElementById("myModal_contato");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Adiciona um ouvinte de eventos para capturar os cliques fora do modal
window.addEventListener('click', fecharModalFora);