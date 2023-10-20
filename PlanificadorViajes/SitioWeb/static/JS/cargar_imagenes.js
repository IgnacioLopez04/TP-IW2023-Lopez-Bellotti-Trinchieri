// document.addEventListener('DOMContentLoaded', function () {
//     var imagenInput = document.querySelector('input[type="file"]');
//     var preview = document.getElementById('preview');
//     var images = []; // Almacena información de las imágenes seleccionadas

//     imagenInput.addEventListener('change', function () {
//         preview.innerHTML = ''; // Limpia la vista previa anterior
//         images = []; // Limpia el array de imágenes seleccionadas

//         for (var i = 0; i < imagenInput.files.length; i++) {
//             var file = imagenInput.files[i];
//             images.push(file); // Agrega el archivo al array de imágenes

//             var img = document.createElement('img');
//             img.src = URL.createObjectURL(file);
//             img.style.maxWidth = '100px'; // Ajusta el tamaño de la vista previa

//             // Agregar un botón de eliminación
//             var deleteButton = document.createElement('button');
//             deleteButton.innerText = 'Eliminar imagen ' + images.length;
//             deleteButton.addEventListener('click', function () {
//                 var imageContainer = deleteButton.parentElement; // El contenedor de la imagen
//                 var index = Array.from(preview.children).indexOf(imageContainer);
//                 images.splice(index, 1); // Elimina la imagen del array

//                 // Eliminar la vista previa
//                 preview.removeChild(imageContainer);
//             });

//             var imageContainer = document.createElement('div');
//             imageContainer.appendChild(img);
//             imageContainer.appendChild(deleteButton);
//             preview.appendChild(imageContainer);
//         }
//     });
// });