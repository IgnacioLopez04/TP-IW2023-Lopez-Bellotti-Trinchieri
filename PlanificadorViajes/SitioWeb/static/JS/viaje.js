const total_form = document.getElementById('id_form-TOTAL_FORMS');
src = "https://code.jquery.com/jquery-3.6.0.min.js";

function abrirMapa() {
    var id_viaje = $('#id-viaje-input').val();
    window.open(`/googleMaps/cargarDestino/${id_viaje}`, 'Mapa', 'width=800,height=600', { 'idViaje': id_viaje });
}

//agregar correos
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
            var elementoDiv = document.createElement('div');
            elementoDiv.className = 'div-correo'
            var elementoCorreo = document.createElement("span");
            elementoCorreo.textContent = correo;
            var elementoCorreoOculto = document.createElement('input'); //se crea un input oculto para obtener los valores de los mails
            elementoCorreoOculto.setAttribute('type', 'hidden')
            elementoCorreoOculto.setAttribute('name', 'correo-span')
            elementoCorreoOculto.setAttribute('value', correo)
            elementoCorreo.appendChild(elementoCorreoOculto)
            // Crear un botón de eliminar
            var botonEliminar = document.createElement("button");
            botonEliminar.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M256 48a208 208 0 1 1 0 416 208 208 0 1 1 0-416zm0 464A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM175 175c-9.4 9.4-9.4 24.6 0 33.9l47 47-47 47c-9.4 9.4-9.4 24.6 0 33.9s24.6 9.4 33.9 0l47-47 47 47c9.4 9.4 24.6 9.4 33.9 0s9.4-24.6 0-33.9l-47-47 47-47c9.4-9.4 9.4-24.6 0-33.9s-24.6-9.4-33.9 0l-47 47-47-47c-9.4-9.4-24.6-9.4-33.9 0z"/></svg>';
            botonEliminar.className = "d-flex justify-content-center align-items-center btn-eliminar";

            // Manejar el clic en el botón de eliminar
            botonEliminar.addEventListener("click", function () {
                correosAgregados.removeChild(elementoDiv);
                correosAgregados.removeChild(botonEliminar);

                // Verificar si es el último elemento y eliminar la coma si es necesario
                if (correosAgregados.childNodes.length === 0) {
                    correosAgregados.textContent = "";
                } else {
                    correosAgregados.removeChild(correosAgregados.lastChild);
                }
            });

            // Agregar el correo y el boton al div de correos agregados
            elementoDiv.appendChild(elementoCorreo)
            elementoDiv.appendChild(botonEliminar)
            correosAgregados.appendChild(elementoDiv);

            // Limpiar el campo de entrada de correo
            inputCorreos.value = "";
        }
        else {
            // Mostrar un mensaje de error o tomar otra acción si el correo no es válido
            alert("El correo ingresado no es válido. Debe tener el formato correcto ***@***.com.");
        }
    });

    // Manejar el click en el botón de eliminar junto a los correos existentes
    correosAgregados.addEventListener("click", function (event) {
        if (event.target.classList.contains("btn-eliminar")) {
            var correoAEliminar = event.target.previousSibling; // El span del correo
            correosAgregados.removeChild(correoAEliminar);
            correosAgregados.removeChild(event.target); // El botón de eliminar
        }
    });
});

// function agregar_dia() {
//     let total_form_dia = document;
//     let count = 0;
//     if (document.getElementsByClassName('form-dia') != null) {
//         total_form_dia = document.getElementsByClassName('form-dia');
//         count = total_form_dia.length;
//     }

//     const form_lista = document.getElementById('form-lista-dias');
//     const empty_form = document.getElementById('empty-form').cloneNode(true);
//     empty_form.setAttribute('class', 'form-dia')
//     empty_form.setAttribute('id', `id-form-dia-${count + 1}`);

//     const regex = new RegExp('__prefix__', 'g');
//     empty_form.innerHTML = empty_form.innerHTML.replace(regex, count);
//     total_form.setAttribute('value', count + 1);

//     const titulo = document.createElement("h1");
//     titulo.id = `id-dia-${count + 1}`;
//     titulo.innerText = `Dia ${count + 1}`;

//     const selector = '#id_form-' + count + '-DELETE'; // se deja count solo porque este
//     // id va un numero menos que el formulario
//     const inputs_delete = empty_form.querySelector(selector);
//     inputs_delete.addEventListener('click', eliminar_dia);

//     form_lista.appendChild(titulo);
//     form_lista.append(empty_form);
// }

// function obtener_campos(lista, attr, texto) {

//     const campos_deseados = [];

//     for (let i = 0; i < lista.length; i++) {
//         const elemento = lista[i];
//         const campo = elemento.getAttribute(attr);

//         var rgx = new RegExp('^' + texto + '-\\d+$')

//         if (campo != null && rgx.test(campo)) {
//             campos_deseados.push(elemento);
//         }
//     }

//     return campos_deseados;
// }

// function eliminar_dia(event) {

//     const form_a_eliminar = event.target.closest('.form-dia');
//     form_a_eliminar.setAttribute('class', 'hidden');

//     const form_lista = document.getElementById('form-lista-dias');
//     var num_dia = form_a_eliminar.id.replace('id-form-dia-', '');
//     const form_dias = form_lista.querySelectorAll('.form-dia');

//     for (let i = 0; i < form_dias.length; i++) {
//         const form_dia = form_dias[i];
//         form_dia.setAttribute('id', `id-form-dia-${i + 1}`)
//     }

//     const titulo_a_eliminar = document.getElementById('id-dia-' + num_dia);

//     form_a_eliminar.removeAttribute('id');

//     form_lista.removeChild(titulo_a_eliminar);

//     const h1 = document.querySelectorAll("h1");
//     const dias = obtener_campos(h1, 'id', 'id-dia');

//     for (let i = 0; i < dias.length; i++) {
//         const dia = dias[i]
//         if (dia.id.replace('id-dia-', '') >= num_dia) {
//             const numero_dia = dia.id.replace('id-dia-', '')
//             dia.setAttribute('id', `id-dia-${numero_dia - 1}`)
//             dia.innerText = `Dia ${numero_dia - 1}`;
//         }
//     }
// }
document.addEventListener('DOMContentLoaded', function () {
    // Obtén el ID del viaje desde la URL
    const urlParams = new URLSearchParams(window.location.search);
    const viajeID = urlParams.get('viaje_id');

    if (viajeID) {
        // Realiza una solicitud para obtener los detalles del viaje
        fetch(`/api/viaje_general/buscar_un_viaje/?id=${viajeID}`)
            .then(response => response.json())
            .then(data => {
                // Llena los campos de datos con los detalles del viaje
                document.getElementById('id_nombreViaje').value = data.nombreViaje;
                document.getElementById('id_descripcion').value = data.descripcion;
                document.getElementById('id_mesDesde').value = data.mesDesde;
                document.getElementById('id_mesHasta').value = data.mesHasta;
                document.getElementById('id_esPrivado').selectedIndex = data.esPrivado === false ? 0 : 1;

                // Ahora, realiza una solicitud para obtener los días asociados al viaje
                fetch(`/api/viaje_general/buscar_dias_por_viaje/?viaje_id=${viajeID}`)
                    .then(response => response.json())
                    .then(dias => {
                        const contDiasAsociados = document.getElementById('dias-viaje-actualizo');

                        // Limpia el contenedor de días
                        contDiasAsociados.innerHTML = '';

                        // Itera a través de los días y muestra la información
                        dias.forEach(dia => {
                            const diaElement = document.createElement('div');
                            diaElement.className = 'm-2 p-2 d-flex justify-content-between align-items-center flex-column dia-viaje';
                            diaElement.innerHTML = `
                                <div class='d-flex justify-content-center align-items-center flex-column w-100'>
                                    <div class="d-flex justify-content-center align-items-center w-75 nombre-dia">
                                        <p class='m-1 font-weight-bold'>${dia.nombreDia}</p>
                                    </div>
                                    <p class='m-1'>${dia.notas}</p>
                                </div>
                                <div class="text-center">
                                    <button type="button" data-target="#modal" class="my-1 bs-modal btn btn-sm btn-primary btn-accion-dia update-dia-viaje" data-form-url="{% url 'update-dia-viaje' dia.pk %}">
                                        <span class="fa fa-pencil">Actualizar</span>
                                    </button>
                                    <button type="button" data-target="#modal" class="my-1 w-100 bs-modal btn btn-sm btn-danger btn-accion-dia delete-dia-viaje" data-form-url="{% url 'delete-dia-viaje' dia.pk %}">
                                        <span class="fa fa-trash">Eliminar</span>
                                    </button>
                                </div>
                            `;
                            contDiasAsociados.appendChild(diaElement);
                        });
                    })
                    .catch(error => console.error('Error al obtener los días asociados:', error));
            })
            .catch(error => console.error('Error al obtener los detalles del viaje:', error));
    }
});