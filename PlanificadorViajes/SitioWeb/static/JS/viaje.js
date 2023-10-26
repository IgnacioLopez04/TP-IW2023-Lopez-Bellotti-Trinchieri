const total_form = document.getElementById('id_form-TOTAL_FORMS');
src = "https://code.jquery.com/jquery-3.6.0.min.js";

function abrirMapa() {
    var id_viaje = $('#id-viaje-input').val();
    if(!id_viaje){
        id_viaje = $('#modal').data('form-url').split('/')[3]
    }
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

/* Ejecuta el ajax a esa url para que haga el get */
$(document).ready(function () {
    var url = document.URL;
    $.ajax({
        url: url,
        type: 'GET',
    });

    if (url.includes("viajes/update")) {
        $("#btn-cargar-info-viaje-general").hide();
        $("#btn-update-viaje").show();
        $("#create-dia-viaje").show();
        $('#create-dia-viaje').attr('data-idviaje', url.split('/')[5]);

        $("#btn-update-viaje").on('click', function () {
            var formData = new FormData($("#viaje-form")[0]);
            var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
            $.ajax({
                url: url,
                type: 'POST',
                data: formData,
                headers: {
                    'X-CSRFToken': csrfToken
                },
                dataType: 'json',
                processData: false,
                contentType: false,
            });
            window.location.href = '/sitio';
        });
    }
});