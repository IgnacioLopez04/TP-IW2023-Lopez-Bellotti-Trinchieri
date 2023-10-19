document.addEventListener('DOMContentLoaded', function () {
    const resultsDiv = document.getElementById('results');

    function mostrarTodosLosViajes() {
        fetch('/api/viaje_general/viajes_usuario/')
            .then(response => response.json())
            .then(data => {
                resultsDiv.innerHTML = '';

                if (data.length === 0) {
                    // Si no se encontraron resultados, muestra un mensaje
                    resultsDiv.innerHTML = '<p>No se encontraron resultados.</p>';
                } else {
                    data.forEach(viaje => {
                        const viajeDiv = document.createElement('div');
                        viajeDiv.classList.add('viajes');

                        viajeDiv.innerHTML = `
                            <a href='/viajes/detalle-viaje/${viaje.id}'>
                            <h2>${viaje.nombreViaje}</h2>
                            <p><span>Descripción:</span> ${viaje.descripcion}</p>
                            <p><span>Cantidad de dias:</span> ${viaje.cantidadDias}</p>
                            <p><span>Calificacion:</span> ${viaje.calificacion}</p>
                        `;

                        const editarButton = document.createElement('button');
                        editarButton.classList.add('editar-viaje');
                        editarButton.textContent = 'Editar';
                        editarButton.dataset.id = viaje.id;

                        // Agregar un manejador de eventos para el botón "Editar"
                        editarButton.addEventListener('click', function () {
                            const viajeID = editarButton.dataset.id;
                            window.location.href = `/viajes/?viaje_id=${viajeID}`;
                        });

                        viajeDiv.appendChild(editarButton);
                        resultsDiv.appendChild(viajeDiv);
                    });
                }
            })
            .catch(error => console.error('Error:', error));
    }

    mostrarTodosLosViajes();

    function filtrarViajes() {
        const destino = document.getElementById('destino-input').value;
        const diasHasta = document.getElementById('dias-hasta-input').value;
        const calificacion = document.getElementById('calificacion-input').value;
        const estado = document.getElementById('estado-viaje').value;

        let apiUrl = '/api/viaje_general/viajes_usuario/?';

        // Construye la URL de la API en función de los valores ingresados
        if (destino) {
            apiUrl += `destino=${destino}`;
        }
        if (diasHasta) {
            apiUrl += `&dias-hasta=${diasHasta}`;
        }
        if (calificacion) {
            apiUrl += `&calificacion=${calificacion}`;
        }
        if (estado) {
            apiUrl += `&estado=${estado}`;
        }

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const resultsDiv = document.getElementById('results');
                // Limpia los resultados anteriores
                resultsDiv.innerHTML = '';


                if (data.length === 0) {
                    // Si no se encontraron resultados, muestra un mensaje
                    resultsDiv.innerHTML = '<p>No se encontraron resultados.</p>';
                } else {
                    // Maneja los datos recibidos y genera el HTML de los resultados
                    data.forEach(viaje => {
                        const viajeDiv = document.createElement('div');
                        viajeDiv.classList.add('viajes');

                        viajeDiv.innerHTML = `
                            <a href='/viajes/detalle-viaje/${viaje.id}'>
                            <h2>${viaje.nombreViaje}</h2>
                            <p><span>Descripción:</span> ${viaje.descripcion}</p>
                            <p><span>Cantidad de dias:</span> ${viaje.cantidadDias}</p>
                            <p><span>Calificacion:</span> ${viaje.calificacion}</p>
                        `;

                        const editarButton = document.createElement('button');
                        editarButton.classList.add('editar-viaje');
                        editarButton.textContent = 'Editar';
                        editarButton.dataset.id = viaje.id;

                        // Agregar un manejador de eventos para el botón "Editar"
                        editarButton.addEventListener('click', function () {
                            const viajeID = editarButton.dataset.id;
                            window.location.href = `/viajes/?viaje_id=${viajeID}`;
                        });

                        viajeDiv.appendChild(editarButton);
                        resultsDiv.appendChild(viajeDiv);
                    });
                }
            })
            .catch(error => console.error('Error:', error));
    }

    // Agregar un evento al formulario para filtrar viajes cuando se envíe
    document.getElementById('search-form').addEventListener('submit', function (e) {
        e.preventDefault();
        filtrarViajes(); // Llama a la función de filtrarViajes en lugar de mostrarTodosLosViajes
    });

    document.getElementById('estado-viaje').addEventListener('change', function () {
        filtrarViajes();
    });

    document.getElementById('limpiar-filtros').addEventListener('click', function () {
        // Restablecer los valores de marcador de posición
        document.getElementById('destino-input').value = '';
        document.getElementById('dias-hasta-input').value = '';
        document.getElementById('calificacion-input').value = '';
        document.getElementById('estado-viaje').selectedIndex = 0;
        mostrarTodosLosViajes();
    });

});

