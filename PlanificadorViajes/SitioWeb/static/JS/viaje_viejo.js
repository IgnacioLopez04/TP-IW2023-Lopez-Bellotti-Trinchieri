function actualizar_num_Id(num_dia, elemento){

    let num_id = elemento.id.split('-')[1];

    if (num_id >= num_dia){
        num_id -= 1;
    }

    const nombre = elemento.id.split('-')[2];

    return `id_form-${num_id}-${nombre}`;
}

function obtener_campos(lista, attr){

    const campos_deseados = [];

    for (let i = 0; i < lista.length; i++) {
        const elemento = lista[i];
        const campo = elemento.getAttribute(attr);
        console.log("attr: " + attr);
        console.log("campo: " + campo);

        if (campo != null && campo.match(/^id_form-\d+-\w+$/)) {
            campos_deseados.push(elemento);
        }
    }

    return campos_deseados;
}

function eliminar_dia(event){
    const form_a_eliminar = event.closest('.form-dia');
    const form_lista = document.getElementById('form-lista-dias');

    var num_dia = form_a_eliminar.id.replace('id-form-dia-', '');

    //sacamos los inputs
    const inputs = document.querySelectorAll("input");
    const selects = document.querySelectorAll("select");
    const labels = document.querySelectorAll("label");

    const inputsDeseados = obtener_campos(inputs, 'id');
    const selectsDeseados = obtener_campos(selects, 'id');
    const labelsDeseados = obtener_campos(labels, 'htmlFor');

    console.log(labelsDeseados);

    //actualizar el numero de 'id_form_numero_campo'
    for (let i = 0; i < inputsDeseados.length; i++){
        const elemento = inputsDeseados[i];

        elemento.setAttribute('id', actualizar_num_Id(num_dia, elemento));
    }

    for (let i = 0; i < selectsDeseados.length; i++){
        const elemento = inputsDeseados[i];

        elemento.setAttribute('id', actualizar_num_Id(num_dia, elemento));
    }

    //actualizar el numero en la etiqueta for del label de ese camp0
    for (let i = 0; i < selectsDeseados.length; i++){
        const elemento = inputsDeseados[i];

        elemento.setAttribute('id', actualizar_num_Id(num_dia, elemento));
    }

    const titulo_a_eliminar = document.getElementById('id-dia-' + num_dia);

    const total_form_dia = document.getElementsByClassName('form-dia');
    let count = total_form_dia.length;
    total_form.setAttribute('value', count - 1);

    form_lista.removeChild(form_a_eliminar);
    form_lista.removeChild(titulo_a_eliminar);
}