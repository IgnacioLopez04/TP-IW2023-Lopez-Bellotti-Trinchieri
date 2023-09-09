const btnAgregarDia = document.getElementById('btn-agregar-dias');
btnAgregarDia.addEventListener('click',agregar_dia);
const total_form = document.getElementById('id_form-TOTAL_FORMS');
function agregar_dia(){
    let total_form_dia = document;
    let count = 0;
    if (document.getElementsByClassName('form-dia') != null){
        total_form_dia = document.getElementsByClassName('form-dia');
        count = total_form_dia.length;
    }
    console.log(count);
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

    form_lista.appendChild(titulo);
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
    const form_dias = form_lista.querySelectorAll('.form-dia');

    for (let i = 0; i < form_dias.length; i++){
        const form_dia = form_dias[i];
        form_dia.setAttribute('id', `id-form-dia-${i+1}`)
    }

    const titulo_a_eliminar = document.getElementById('id-dia-' + num_dia);

    form_a_eliminar.removeAttribute('id');

    form_lista.removeChild(titulo_a_eliminar);

    const h1 = document.querySelectorAll("h1");
    const dias = obtener_campos(h1, 'id');
    var dias_a_modificar = [];

    for (let i = 0; i < dias.length; i++){
        const dia = dias[i]
        if (dia.id.replace('id-dia-', '') >= num_dia){
             const numero_dia = dia.id.replace('id-dia-', '')
            dia.setAttribute('id', `id-dia-${numero_dia - 1}`)
            dia.innerText = `Dia ${numero_dia - 1}`;
        }
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