function MostrarOcultarSenha() {

    let senha = document.getElementById("campo-formulario-senha");
    if (senha.type == "password") {
        senha.type = "text;"
    } else {
        senha.type = "password";
    };

};