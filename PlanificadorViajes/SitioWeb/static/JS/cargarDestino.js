"use strict";
src = "https://code.jquery.com/jquery-3.6.0.min.js";

// import { listarDestinosPorDia } from "./viaje";

let listaDestinos = []
const getFormInputElement = (component) => document.getElementById(component + '-input');

function initMap() {

    const CONFIGURATION = {
        "ctaTitle": "Confirmar",
        "mapOptions": { "center": { "lat": -31.3990547, "lng": -64.3590263 }, "fullscreenControl": true,
                        "mapTypeControl": false, "streetViewControl": true, "zoom": 6, "zoomControl": true,
                        "maxZoom": 22, "mapId": "" },
        "mapsApiKey": "",
        "capabilities": { "addressAutocompleteControl": true, "mapDisplayControl": true, "ctaControl": true }

    };
    const componentForm = [
        'location',
        'locality',
        'administrative_area_level_1',
    ];

    const map = new google.maps.Map(document.getElementById("gmp-map"), {
        zoom: CONFIGURATION.mapOptions.zoom,
        center: { lat: -31.3990547, lng: -64.3590263 },
        mapTypeControl: false,
        fullscreenControl: CONFIGURATION.mapOptions.fullscreenControl,
        zoomControl: CONFIGURATION.mapOptions.zoomControl,
        streetViewControl: CONFIGURATION.mapOptions.streetViewControl
    });

    const marker = new google.maps.Marker({ map: map, draggable: false });
    const autocompleteInput = getFormInputElement('location');
    const autocomplete = new google.maps.places.Autocomplete(autocompleteInput, {
        fields: ["address_components", "geometry", "name"],
        types: ["locality"],
    });

    autocomplete.addListener('place_changed', function () {
        marker.setVisible(false);
        const place = autocomplete.getPlace();
        if (!place.geometry) {
            // User entered the name of a Place that was not suggested and
            // pressed the Enter key, or the Place Details request failed.
            window.alert('No hay detalles para la entrada: \'' + place.name + '\'');
            return;
        }
        renderAddress(place);
        fillInAddress(place);
    });


    function fillInAddress(place) {  // optional parameter
        const addressNameFormat = {
            'locality': 'short_name',
            'administrative_area_level_1': 'short_name',
        };
        const getAddressComp = function (type) {
            for (const component of place.address_components) {
                if (component.types[0] === type) {
                    return component[addressNameFormat[type]];
                }
            }
            return '';
        };
        getFormInputElement('location').value = getAddressComp('street_number') + ' '
            + getAddressComp('route');
        for (const component of componentForm) {
            // Location field is handled separately above as it has different logic.
            if (component !== 'location') {
                getFormInputElement(component).value = getAddressComp(component);
            }
        }
    }

    function renderAddress(place) {
        map.setCenter(place.geometry.location);
        marker.setPosition(place.geometry.location);
        marker.setVisible(true);
    }
}

document.addEventListener('DOMContentLoaded', function () {

    //llamo a la funcion initMap
    initMap();

    // Agrega el evento click al botón "Agregar destino"
    const agregarDestinoBtn = document.getElementById('agregar-destino');
    var destinosAgregados = document.getElementById("destinos-agregados");

    agregarDestinoBtn.addEventListener('click', function () {

        // Verifica que los campos localidad y provincia estén completos
        var localidad = document.getElementById('locality-input');
        var provincia = document.getElementById('administrative_area_level_1-input');
        if (!localidad.value || !provincia.value) {
            alert('Por favor, ingresa el dato de la localidad correctamente.');
            return;
        }

        // Crear un elemento de texto para mostrar el correo
        var elementoDiv = document.createElement('div');
        elementoDiv.className = 'div-destino'
        //Creo un input para guardar el valor del span y esta oculto
        var elemetoInput = document.createElement('input');
        elemetoInput.className = 'input-destino'
        elemetoInput.setAttribute('type', 'hidden');

        var elementoLocalidad = document.createElement("span");
        elementoLocalidad.textContent = localidad.value + ', ' + provincia.value;
        //Le coloco el valor del span al input
        elemetoInput.setAttribute('name', elementoLocalidad.textContent)
        listaDestinos.push(elementoLocalidad.textContent);
        // Crear un botón de eliminar
        var botonEliminar = document.createElement("button");
        botonEliminar.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M256 48a208 208 0 1 1 0 416 208 208 0 1 1 0-416zm0 464A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM175 175c-9.4 9.4-9.4 24.6 0 33.9l47 47-47 47c-9.4 9.4-9.4 24.6 0 33.9s24.6 9.4 33.9 0l47-47 47 47c9.4 9.4 24.6 9.4 33.9 0s9.4-24.6 0-33.9l-47-47 47-47c9.4-9.4 9.4-24.6 0-33.9s-24.6-9.4-33.9 0l-47 47-47-47c-9.4-9.4-24.6-9.4-33.9 0z"/></svg>';
        botonEliminar.className = "btn-eliminar";

        // Manejar el clic en el botón de eliminar
        botonEliminar.addEventListener("click", function () {
            destinosAgregados.removeChild(elementoDiv);
            listaDestinos.removeChild(elementoLocalidad);


            // Verificar si es el último elemento y eliminar la coma si es necesario
            if (destinosAgregados.childNodes.length === 0) {
                destinosAgregados.textContent = "";
            } else {
                destinosAgregados.removeChild(destinosAgregados.lastChild);
            }
        });

        elementoDiv.appendChild(elementoLocalidad);
        elementoDiv.appendChild(elemetoInput);
        elementoDiv.appendChild(botonEliminar);
        destinosAgregados.appendChild(elementoDiv);

        // Agregar una coma y un espacio para separar múltiples correos
        // destinosAgregados.appendChild(document.createTextNode(", "));

        // Limpia los campos después de agregar el destino
        document.getElementById('locality-input').value = '';
        document.getElementById('administrative_area_level_1-input').value = '';
    });

    // Agrega el evento click al botón "Confirmar destinos"
    $('#confirmar-destinos').on('click', function(){
        //Almacena los valores del input 'input-destino'
        
        var formData = {
            'destinos' :[]
        }
        $('.input-destino').each(function () {
            formData['destinos'].push($(this).attr('name'));
        });

        // var urlActual = window.location.href;
        // console.log(urlActual);
        // // Analizar la URL para obtener los parámetros
        // var urlParams = new URLSearchParams(urlActual);
        // console.log(urlParams);
        // // Obtener el valor del parámetro "id"
        // var idViaje = urlParams.get("id");
        var urlActual = window.location.href;
        var url = new URL(urlActual);
        console.log(url);
        var idViaje = url.searchParams.get("id_viaje");

        console.log(idViaje);

        var url = `/googleMaps/confirmarDestino/${idViaje}`;
        console.log(url);

        $.ajax({
            url: url,
            type: 'POST',
            data: JSON.stringify(formData),
            contentType: 'application/json',
            dataType: 'json',
            success: function(data){
                alert('nashe');
                window.close();
            }
        })
    });

    // const confirmarDestinosBtn = document.getElementById('confirmar-destinos');
    // confirmarDestinosBtn.addEventListener('click', function () {

    //     const urlActual = window.location.href;
    //     const matches = urlActual.match(/\/(\d+)$/);
    //     var ultimoNumero = parseInt(matches[1]);

    //     const objetoJSON = {
    //         destinos: listaDestinos,
    //         num_dia: ultimoNumero
    //     };

    //     let nuevoJson = JSON.stringify(objetoJSON)

    //     // window.opener.recibirDestinos(nuevoJson);

    //     //listarDestinosPorDia(listaDestinos, ultimoNumero);
    //     window.close();
    // });
});

