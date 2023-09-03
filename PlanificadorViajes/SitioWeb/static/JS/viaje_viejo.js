var forms_totales = document.querySelector('#id_form-TOTAL_FORMS');

function createFormField(labelText, fieldName, forms_totales) {
        var label = document.createElement('label');
        label.innerHTML = labelText;

        var input = document.querySelector('#id_form-0-' + fieldName).cloneNode(true);
        input.name = 'form-' + forms_totales.value + '-' + fieldName;
        input.id = 'id_form-' + forms_totales.value + '-' + fieldName;

        var pTag = document.createElement('p');
        pTag.appendChild(label);
        pTag.appendChild(input);

        return pTag;
    }

function agregar_inputs() {
    var formDia = document.querySelector('#form-dia');

    var dia = document.createElement('h1');
    dia.innerHTML = 'Dia ' + (parseInt(forms_totales.value) + parseInt(1));

    formDia.appendChild(dia);
    formDia.appendChild(createFormField('Nombre:', 'nombreDia', forms_totales));
    formDia.appendChild(createFormField('Notas:', 'notas', forms_totales));
    formDia.appendChild(createFormField('Destinos:', 'destinos', forms_totales));
    //formDia.appendChild(createFormField('Otro Destino:', 'destinos'));

    forms_totales.value = parseInt(forms_totales.value) + 1;
}

function agregar_destinos(){
    var formDia = document.querySelector('#form-dia');

    num_del_formulario = forms_totales.value - 1;

    var input = document.querySelector('#id_form-'+ num_del_formulario + '-destinos').cloneNode(true);
    input.name = 'form-'+ num_del_formulario + '-destinos';
    input.id = 'id_form-'+ num_del_formulario + '-destinos';

    formDia.appendChild(createFormField('Destinos:', 'destinos', forms_totales));

}
