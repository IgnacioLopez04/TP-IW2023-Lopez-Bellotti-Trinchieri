document.addEventListener('DOMContentLoaded', function () {
    const resultsDiv = document.getElementById('results');

    // Función para obtener y mostrar todos los viajes
    function mostrarTodosLosViajes() {
        fetch('/api/viaje_general/todos_los_viajes/')
            .then(response => response.json())
            .then(data => {
                resultsDiv.innerHTML = '';

                if (data.length === 0) {
                    // Si no se encontraron resultados, muestra un mensaje
                    resultsDiv.innerHTML = '<p>No se encontraron resultados.</p>';
                } else {
                    data.forEach(viaje => {
                        resultsDiv.innerHTML += `
                        <div class="p-2 m-2 d-flex justify-content-center align-items-center flex-column viajes">
                            <a href='/viajes/detalle-viaje/${viaje.id}' class='text-decoration-none h-100 d-flex justify-content-between align-items-center flex-column''>
                            <h2>${viaje.nombreViaje}</h2>
                            <div class='d-flex justify-content-center align-items-start flex-column flex-grow-1'>
                                <p><span>Descripción:</span> ${viaje.descripcion}</p>
                                <p><span>Cantidad de días:</span> ${viaje.cantidadDias}</p>
                                <p><span>Calificación:</span> ${viaje.calificacion}</p>
                            </div>
                        </div>`;
                    });
                }
            })
            .catch(error => console.error('Error:', error));
    }

    // Llama a la función para mostrar todos los viajes al cargar la página
    mostrarTodosLosViajes();

    // Función para filtrar y mostrar viajes según los criterios ingresados
    function filtrarViajes() {
        const destino = document.getElementById('destino-input').value;
        const diasHasta = document.getElementById('dias-hasta-input').value;
        const calificacion = document.getElementById('calificacion-input').value;

        let apiUrl = '/api/viaje_general/filtrar_viajes/?';

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

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const resultsDiv = document.getElementById('results');
                // Limpia los resultados anteriores
                resultsDiv.innerHTML = '';


                if (data.length === 0) {
                    console.log("no anduvo");
                    // Si no se encontraron resultados, muestra un mensaje
                    resultsDiv.innerHTML = '<p>No se encontraron resultados.</p>';
                } else {
                    console.log("data: ", data);
                    // Maneja los datos recibidos y genera el HTML de los resultados
                    data.forEach(viaje => {
                        resultsDiv.innerHTML += `
                        <div class="p-2 m-2 d-flex justify-content-center align-items-center flex-column viajes">
                            <a href='/viajes/detalle-viaje/${viaje.id}' class='text-decoration-none h-100 d-flex justify-content-between align-items-center flex-column''>
                            <h2>${viaje.nombreViaje}</h2>
                            <div class='d-flex justify-content-center align-items-start flex-column flex-grow-1'>
                                <p><span>Descripción:</span> ${viaje.descripcion}</p>
                                <p><span>Cantidad de días:</span> ${viaje.cantidadDias}</p>
                                <p><span>Calificación:</span> ${viaje.calificacion}</p>
                            </div>
                        </div>`;
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

    document.getElementById('limpiar-filtros').addEventListener('click', function () {
        // Restablecer los valores de marcador de posición
        document.getElementById('destino-input').value = '';
        document.getElementById('dias-hasta-input').value = '';
        document.getElementById('calificacion-input').value = '';
        mostrarTodosLosViajes();
    });

});