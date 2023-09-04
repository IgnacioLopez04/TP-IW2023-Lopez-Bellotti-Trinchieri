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
                        <div class="viajes">
                            <a href='/viajes/detalle-viaje/${viaje.id}'>
                            <h2>${viaje.nombreViaje}</h2>
                            <p><span>Descripción:</span> ${viaje.descripcion}</p>
                            <p><span>Cantidad de dias:</span> ${viaje.cantidadDias}</p>
                            <p><span>Calificacion:</span> ${viaje.calificacion}</p>
                        </div>`;

                        //hago que muestre el nombre del viaje con el link para ir al detalle
                        // const viajeDetailLink = document.createElement('a');
                        // viajeDetailLink.href = `/viajes/detalle-viaje/${viaje.id}/`;
                        // viajeDetailLink.textContent = `Nombre del Viaje: ${viaje.nombreViaje}`;
                        // resultsDiv.appendChild(viajeDetailLink);

                        // resultsDiv.innerHTML += `<div>
                        // <p>Descripción: ${viaje.descripcion}</p>
                        // <p>Cantidad de dias: ${viaje.cantidadDias}</p>
                        // <p>Calificacion: ${viaje.calificacion}</p>
                        // </div>`;
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

        let apiUrl = '/api/viaje_general/filtrar_viajes/?';

        // Construye la URL de la API en función de los valores ingresados
        if (destino) {
            apiUrl += `destino=${destino}`;
            console.log('El valor de la url es: ' + apiUrl);
        }
        if (diasHasta) {
            apiUrl += `&dias-hasta=${diasHasta}`;
            console.log(apiUrl);
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
                        resultsDiv.innerHTML += `
                        <div class="viajes">
                            <a href='/viajes/detalle-viaje/${viaje.id}'>
                            <h2>${viaje.nombreViaje}</h2>
                            <p><span>Descripción:</span> ${viaje.descripcion}</p>
                            <p><span>Cantidad de dias:</span> ${viaje.cantidadDias}</p>
                            <p><span>Calificacion:</span> ${viaje.calificacion}</p>
                        </div>`;
                        //hago que muestre el nombre del viaje con el link para ir al detalle
                        // const viajeDetailLink = document.createElement('a');
                        // viajeDetailLink.href = `/viajes/detalle-viaje/${viaje.id}/`;
                        // viajeDetailLink.textContent = `Nombre del Viaje: ${viaje.nombreViaje}`;
                        // resultsDiv.appendChild(viajeDetailLink);

                        // resultsDiv.innerHTML += `
                        // <div>
                        //     <p>Descripción: ${viaje.descripcion}</p>
                        //     <p>Cantidad de dias: ${viaje.cantidadDias}</p>
                        //     <p>Calificacion: ${viaje.calificacion}</p>
                        // </div>`;
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
});