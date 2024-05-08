// Arquivo para controlar as funcionalidades do modal

// Função para abrir o modal
function abrirModal() {
    var modal = document.getElementById("myModal_agenda");
    modal.style.display = "block";
}

// Função para fechar o modal
function fecharModal() {
    var modal = document.getElementById("myModal_agenda");
    modal.style.display = "none";
}

// Função para fechar o modal ao clicar fora dele
function fecharModalFora(event) {
    var modal = document.getElementById("myModal_agenda");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Adiciona um ouvinte de eventos para capturar os cliques fora do modal
window.addEventListener('click', fecharModalFora);
