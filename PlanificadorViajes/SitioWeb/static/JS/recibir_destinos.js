function recibirDestinos(datos){
    const objeto = JSON.parse(datos);

    let destinos = objeto.destinos;
    const num_dia = objeto.num_dia;

    const formularioAgregarDia = document.getElementById('id-form-dia-' + num_dia);
    const label_nuevos_destinos = document.createElement("h3");
    label_nuevos_destinos.innerText = "Destinos cargados";

    formularioAgregarDia.appendChild(label_nuevos_destinos);

    destinos.forEach(element => {
        var elementoDestino = document.createElement("div");
        elementoDestino.textContent = element;
        formularioAgregarDia.appendChild(elementoDestino);
    });
}