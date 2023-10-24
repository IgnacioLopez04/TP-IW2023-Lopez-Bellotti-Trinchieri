document.addEventListener('click', function (event) {
    if (event.target.classList.contains('editar-viaje')) {
        const viajeID = event.target.getAttribute('data-id');
        window.location.href = `/viajes/update/${viajeID}`;
    }
});

src="https://code.jquery.com/jquery-3.6.0.min.js";
$(document).ready(function () {
  $(".editar-viaje").on('click', function (event) {
    console.log("entroooo");
      event.preventDefault();

    $.ajax({
      url: url,
      type: 'GET',
      success: function (data) {
        var url = "{% url 'mostrar-dias-viaje' %}";
        $.ajax({
            url: url,
            type: 'POST',
            data: formData,
            dataType: 'json',
            processData: false,
            contentType: false,
            success: function(data) {
                $('.cont-dias').html(data.html_response);
            console.log('Función ejecutada con éxito');
            },
            error: function (error) {
            console.error('Error al ejecutar la función: ' + error);
            }
        });
      }
    });
  });
});