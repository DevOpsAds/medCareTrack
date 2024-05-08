
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

