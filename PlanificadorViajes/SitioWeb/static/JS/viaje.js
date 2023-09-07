const btnAgregarDia = document.getElementById('btn-agregar-dias');
btnAgregarDia.addEventListener('click',agregar_dia);
const total_form = document.getElementById('id_form-TOTAL_FORMS');
function agregar_dia(event){
    if (event){
        event.preventDefault();
    }

    const total_form_dia = document.getElementsByClassName('form-dia');
    let count = total_form_dia.length;

    const form_lista = document.getElementById('form-lista-dias');
    const empty_form = document.getElementById('empty-form').cloneNode(true);
    const div_empty_form = document.getElementById('id-form-dia-empy')
    empty_form.setAttribute('class', 'form-dia')
    empty_form.setAttribute('id',`id-form-dia-${count + 1}`);

    const regex = new RegExp('__prefix__', 'g');
    empty_form.innerHTML = empty_form.innerHTML.replace(regex, count);
    total_form.setAttribute('value', count + 1);

    const titulo = document.createElement("h1");
    titulo.id = `id-dia-${count + 1}`;
    titulo.innerText = `Dia ${count + 1}`;

    const bottonEliminar = document.getElementById('btn-eliminar-dia-hidden').cloneNode(true);
    bottonEliminar.id = `btn-eliminar-dia-${count + 1}`;
    bottonEliminar.removeAttribute('class');

    form_lista.appendChild(titulo);
    empty_form.appendChild(bottonEliminar);
    form_lista.append(empty_form);
}

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


/* const btnAgregarDestino = document.getElementById('btn-agregar-destino');
btnAgregarDestino.addEventListener('click', agregar_destino)
// no funciona esta al pedo por ahora, lo dejo por las dudas
function agregar_destino(event){
    if (event){
        event.preventDefault();
    }
    numero_form = total_form.value;
    total_form_destinos = document.getElementsByClassName('form-lista-destinos');

    const form_dia_actual = event.target.closest('.form-dia');
    const btnAgregarDestino = form_dia_actual.querySelector('#btn-agregar-destino');
    const form_lista_destinos = form_dia_actual.querySelector('.form-lista-dias');
    const nuevo_destino = document.getElementById('id')
}
*/