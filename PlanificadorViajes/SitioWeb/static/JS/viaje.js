const btnAgregarDia = document.getElementById('btn-agregar-dias');
btnAgregarDia.addEventListener('click', agregar_dia);
const total_form = document.getElementById('id_form-TOTAL_FORMS');

function agregar_dia() {
    let total_form_dia = document;
    let count = 0;
    if (document.getElementsByClassName('form-dia') != null) {
        total_form_dia = document.getElementsByClassName('form-dia');
        count = total_form_dia.length;
    }

    const form_lista = document.getElementById('form-lista-dias');
    const empty_form = document.getElementById('empty-form').cloneNode(true);
    empty_form.setAttribute('class', 'form-dia')
    empty_form.setAttribute('id', `id-form-dia-${count + 1}`);

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

    /*let btnAgregarDestino = document.createElement('button');
    btnAgregarDestino.setAttribute('id', 'id-btn-eliminar-destino');
    btnAgregarDestino.setAttribute('type', 'button');
    btnAgregarDestino.innerText = 'Agregar Destino';
    btnAgregarDestino.addEventListener('click', agregar_destino)

    empty_form.append(btnAgregarDestino); */

    form_lista.appendChild(titulo);
    form_lista.append(empty_form);
}

function obtener_campos(lista, attr, texto) {

    const campos_deseados = [];

    for (let i = 0; i < lista.length; i++) {
        const elemento = lista[i];
        const campo = elemento.getAttribute(attr);

        var rgx = new RegExp('^' + texto + '-\\d+$')

        if (campo != null && rgx.test(campo)) {
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

    for (let i = 0; i < form_dias.length; i++) {
        const form_dia = form_dias[i];
        form_dia.setAttribute('id', `id-form-dia-${i + 1}`)
    }

    const titulo_a_eliminar = document.getElementById('id-dia-' + num_dia);

    form_a_eliminar.removeAttribute('id');

    form_lista.removeChild(titulo_a_eliminar);

    const h1 = document.querySelectorAll("h1");
    const dias = obtener_campos(h1, 'id', 'id-dia');
    console.log(dias);
    for (let i = 0; i < dias.length; i++) {
        const dia = dias[i]
        if (dia.id.replace('id-dia-', '') >= num_dia) {
            const numero_dia = dia.id.replace('id-dia-', '')
            dia.setAttribute('id', `id-dia-${numero_dia - 1}`)
            dia.innerText = `Dia ${numero_dia - 1}`;
        }
    }
}

//function agregar_destino(event) {

//const empty_destino = document.getElementById('empty-destino').cloneNode(true);
//const form_actual = event.target.closest('.form-dia');

//empty_destino.removeAttribute('class');

//form_actual.appendChild(empty_destino);
//}