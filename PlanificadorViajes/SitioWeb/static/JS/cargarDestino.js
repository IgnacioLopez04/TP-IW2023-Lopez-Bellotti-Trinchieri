"use strict";

// import { listarDestinosPorDia } from "./viaje";

let listaDestinos = []
const getFormInputElement = (component) => document.getElementById(component + '-input');

function initMap() {

    const CONFIGURATION = {
        "ctaTitle": "Confirmar",
        "mapOptions": { "center": { "lat": -31.3990547, "lng": -64.3590263 }, "fullscreenControl": true, "mapTypeControl": false, "streetViewControl": true, "zoom": 6, "zoomControl": true, "maxZoom": 22, "mapId": "" },
        "mapsApiKey": "LLAVE",
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
        var elementoLocalidad = document.createElement("span");
        elementoLocalidad.textContent = localidad.value + ', ' + provincia.value;
        listaDestinos.push(elementoLocalidad.textContent);
        console.log(listaDestinos);
        // Crear un botón de eliminar
        var botonEliminar = document.createElement("button");
        botonEliminar.textContent = "Eliminar";
        botonEliminar.className = "btn-eliminar";

        // Manejar el clic en el botón de eliminar
        botonEliminar.addEventListener("click", function () {
            destinosAgregados.removeChild(elementoLocalidad);
            destinosAgregados.removeChild(botonEliminar);
            listaDestinos.removeChild(elementoLocalidad);


            // Verificar si es el último elemento y eliminar la coma si es necesario
            if (destinosAgregados.childNodes.length === 0) {
                destinosAgregados.textContent = "";
            } else {
                destinosAgregados.removeChild(destinosAgregados.lastChild);
            }
        });

        destinosAgregados.appendChild(elementoLocalidad);
        destinosAgregados.appendChild(botonEliminar);

        // Agregar una coma y un espacio para separar múltiples correos
        destinosAgregados.appendChild(document.createTextNode(", "));

        // Limpia los campos después de agregar el destino
        document.getElementById('locality-input').value = '';
        document.getElementById('administrative_area_level_1-input').value = '';
    });

    // Agrega el evento click al botón "Confirmar destinos"
    const confirmarDestinosBtn = document.getElementById('confirmar-destinos');
    confirmarDestinosBtn.addEventListener('click', function () {

        listarDestinosPorDia(listaDestinos, numDia());
        listaDestinos = [];
        window.close();
    });

    function numDia() {
        // capturamos la url
        var loc = document.location.href;
        // si existe el interrogante
        if (loc.indexOf('?') > 0) {
            // cogemos la parte de la url que hay despues del interrogante
            var getString = loc.split('?')[1];
            // obtenemos un array con cada clave=valor
            var GET = getString.split('&');
            var get = {};
            // recorremos todo el array de valores
            for (var i = 0, l = GET.length; i < l; i++) {
                var tmp = GET[i].split('=');
                get[tmp[0]] = unescape(decodeURI(tmp[1]));
            }
            return get;
        }
    }
});

