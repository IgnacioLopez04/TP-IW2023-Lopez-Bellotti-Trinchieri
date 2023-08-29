function agregar_inputs() {
    var total_form = document.querySelector('#id_form-TOTAL_FORMS');
    var formDia = document.querySelector('#form-dia');
    function createFormField(labelText, fieldName) {
        var label = document.createElement('label');
        label.innerHTML = labelText;

        var input = document.querySelector('#id_form-0-' + fieldName).cloneNode(true);
        input.name = 'form-' + total_form.value + '-' + fieldName;
        input.id = 'id_form-' + total_form.value + '-' + fieldName;

        var pTag = document.createElement('p');
        pTag.appendChild(label);
        pTag.appendChild(input);

        return pTag;
    }

    formDia.appendChild(createFormField('Nombre:', 'nombreDia'));
    formDia.appendChild(createFormField('Actividades:', 'actividades'));
    formDia.appendChild(createFormField('Destinos:', 'destinos'));
    formDia.appendChild(createFormField('Notas:', 'notas'));
    formDia.appendChild(document.createElement('br'));

    total_form.value = parseInt(total_form.value) + 1;
}