// Obtém o elemento do botão de fechar modal
var closeModalBtn = document.querySelector(".close");

// Adiciona um ouvinte de evento para o clique no botão de fechar modal
closeModalBtn.addEventListener("click", function() {
    // Obtém o modal
    var modal = document.getElementById("myModal_recurso");
    
    // Fecha o modal
    modal.style.display = "none";
});


