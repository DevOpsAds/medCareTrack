document.getElementById('btn_acesso').addEventListener('click', function() {
    // Abre o modal
    console.log("carregado")
    var modal = document.getElementById("myModal_acesso");
    modal.style.display = "block";
});

// Função para fechar o modal ao clicar fora dele
function fecharModalFora(event) {
    var modal = document.getElementById("myModal_acesso");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Adiciona um ouvinte de eventos para capturar os cliques fora do modal
window.addEventListener('click', fecharModalFora);