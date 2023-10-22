document.addEventListener('click', function (event) {
    if (event.target.classList.contains('editar-viaje')) {
        // Obtener el ID del viaje desde el atributo data-id
        const viajeID = event.target.getAttribute('data-id');

        // Redirigir al usuario a la página de carga de viaje con el ID seleccionado
        window.location.href = `/viajes/?viaje_id=${viajeID}`;
    }
});