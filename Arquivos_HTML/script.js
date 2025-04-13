


    // Aqui você pode adicionar funcionalidades como navegação ao clicar nos botões
    document.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', (e) => {
            alert(`${e.target.innerText} clicado!`);
        });
    });
