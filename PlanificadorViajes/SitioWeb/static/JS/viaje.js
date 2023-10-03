const btnAgregarDia = document.getElementById('btn-agregar-dias');
btnAgregarDia.addEventListener('click', agregar_dia);
const total_form = document.getElementById('id_form-TOTAL_FORMS');

//agregar correos
src = "https://code.jquery.com/jquery-3.6.0.min.js"
$(document).ready(function () {
    // Detecta cambios en el campo "Es privado"
    $("select[name='esPrivado']").change(function () {
        if ($(this).val() === 'True') {
            // Mostrar el div si es privado
            $("#usuarios-a-invitar").show();
        } else {
            // Ocultar el div si no es privado
            $("#usuarios-a-invitar").hide();
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    var btnAgregarCorreo = document.getElementById("btn-agregar-correo");
    var inputCorreos = document.getElementById("correos");
    var correosAgregados = document.getElementById("correos-agregados");

    btnAgregarCorreo.addEventListener("click", function () {
        var correo = inputCorreos.value.trim();

        // Validar el formato del correo usando una expresión regular
        var correoValido = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/.test(correo);

        if (correoValido) {
            // Crear un elemento de texto para mostrar el correo
            var elementoCorreo = document.createElement("span");
            elementoCorreo.className = 'correo-span';
            elementoCorreo.textContent = correo;
            // Crear un botón de eliminar
            var botonEliminar = document.createElement("button");
            botonEliminar.textContent = "Eliminar";
            botonEliminar.className = "btn-eliminar";

            // Manejar el clic en el botón de eliminar
            botonEliminar.addEventListener("click", function () {
                correosAgregados.removeChild(elementoCorreo);
                correosAgregados.removeChild(botonEliminar);

                // Verificar si es el último elemento y eliminar la coma si es necesario
                if (correosAgregados.childNodes.length === 0) {
                    correosAgregados.textContent = "";
                } else {
                    correosAgregados.removeChild(correosAgregados.lastChild);
                }
            });

            // Agregar el correo y el boton al div de correos agregados
            correosAgregados.appendChild(elementoCorreo);
            correosAgregados.appendChild(botonEliminar);


            // Agregar una coma y un espacio para separar múltiples correos
            correosAgregados.appendChild(document.createTextNode(", "));

            // Limpiar el campo de entrada de correo
            inputCorreos.value = "";
        }
        else {
            // Mostrar un mensaje de error o tomar otra acción si el correo no es válido
            alert("El correo ingresado no es válido. Debe tener el formato correcto ***@***.com.");
        }
    });

    // Manejar el clic en el botón de eliminar junto a los correos existentes
    correosAgregados.addEventListener("click", function (event) {
        if (event.target.classList.contains("btn-eliminar")) {
            var correoAEliminar = event.target.previousSibling; // El span del correo
            correosAgregados.removeChild(correoAEliminar);
            correosAgregados.removeChild(event.target); // El botón de eliminar
        }
    });
});

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