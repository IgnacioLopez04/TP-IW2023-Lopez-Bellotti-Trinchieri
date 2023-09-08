const btnAgregarDia = document.getElementById('btn-agregar-dias');
btnAgregarDia.addEventListener('click',agregar_dia);
const total_form = document.getElementById('id_form-TOTAL_FORMS');
function agregar_dia(){
    const total_form_dia = document.getElementsByClassName('form-dia');
    let count = total_form_dia.length;

    const form_lista = document.getElementById('form-lista-dias');
    const empty_form = document.getElementById('empty-form').cloneNode(true);
    empty_form.setAttribute('class', 'form-dia')
    empty_form.setAttribute('id',`id-form-dia-${count + 1}`);

    const regex = new RegExp('__prefix__', 'g');
    empty_form.innerHTML = empty_form.innerHTML.replace(regex, count);
    total_form.setAttribute('value', count + 1);

    const titulo = document.createElement("h1");
    titulo.id = `id-dia-${count + 1}`;
    titulo.innerText = `Dia ${count + 1}`;

    const selector = '#id_form-' + count + '-DELETE'; // se deja count solo porque este
                                                            // id va un numero menos que el formulario
    const inputs_delete = empty_form.querySelector(selector);
    inputs_delete.addEventListener('click', eliminar_dia);

    /*const bottonEliminar = document.getElementById('btn-eliminar-dia-hidden').cloneNode(true);
    bottonEliminar.id = `btn-eliminar-dia-${count + 1}`;
    bottonEliminar.removeAttribute('class'); */

    form_lista.appendChild(titulo);
    //empty_form.appendChild(bottonEliminar);
    form_lista.append(empty_form);
}

function obtener_campos(lista, attr){

    const campos_deseados = [];

    for (let i = 0; i < lista.length; i++) {
        const elemento = lista[i];
        const campo = elemento.getAttribute(attr);

        if (campo != null && campo.match(/^id-dia-\d+$/)) {
            campos_deseados.push(elemento);
        }
    }

    return campos_deseados;
}

function eliminar_dia(event) {
    const form_a_eliminar = event.target.closest('.form-dia');
    form_a_eliminar.setAttribute('class', 'hidden');

    const form_lista = document.getElementById('form-lista-dias');
    var num_dia = form_a_eliminar.id.replace('id-form-dia-', '');
    const titulo_a_eliminar = document.getElementById('id-dia-' + num_dia);
    form_lista.removeChild(titulo_a_eliminar);

    const h1 = document.querySelectorAll("h1");
    const dias = obtener_campos(h1, 'id');
    var dias_a_modificar = [];

    for (let i = 0; i < dias.length; i++){
        const dia = dias[i]
        if (dia.id.replace('id-dia-', '') >= num_dia){
            dias_a_modificar.push(dia);
        }
    }

    console.log(dias_a_modificar);
    //actualizar el numero del Dia
    for (let i = 0; i < dias_a_modificar.length; i++){
        const elemento = dias_a_modificar[i];
        const numero_dia = elemento.id.replace('id-dia-', '')
        elemento.innerText = `Dia ${numero_dia - 1}`;
    }
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