const btnAgregarDia = document.getElementById('btn-agregar-dias');
btnAgregarDia.addEventListener('click',agregar_dia)
const total_form = document.getElementById('id_form-TOTAL_FORMS');
function agregar_dia(event){
    if (event){
        event.preventDefault();
    }

    const total_form_dia = document.getElementsByClassName('form-dia');
    let count = total_form_dia.length;

    const form_lista = document.getElementById('form-lista-dias');
    const empty_form = document.getElementById('empty-form').cloneNode(true);
    empty_form.setAttribute('class', 'form-dia')
    empty_form.setAttribute('id',`id-form-dia-${count}`);

    const regex = new RegExp('__prefix__', 'g');
    empty_form.innerHTML = empty_form.innerHTML.replace(regex, count);
    total_form.setAttribute('value', count + 1);

    const titulo = document.createElement("h1");
    titulo.innerText = `Dia ${count + 1}`;
    form_lista.appendChild(titulo)

    form_lista.append(empty_form);

    const numero_de_form = document.createElement('div')
    numero_de_form.className= 'hidden';
    numero_de_form.id=`id-${count + 1}`;

    form_lista.appendChild(numero_de_form);

}

const btnAgregarDestino = document.getElementById('btn-agregar-destino');
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
