const btn_invitar = document.getElementById('btn-invitar');
btn_invitar.addEventListener('click', () => {
    let correoInput = document.getElementById('correo');
    let correo = correoInput.value.trim();
})

let contador_movimiento = 0;

const btn_prev = document.querySelector('.btn-flecha-izq');
const btn_sig = document.querySelector('.btn-flecha-der');
const cont_fotos = document.getElementById('cont-imagenes');
const numImagenes = cont_fotos.querySelectorAll('img').length;

const anchoDinamico = numImagenes * 100; // Multiplica la cantidad de imágenes por 100

// Aplica el ancho al contenedor
cont_fotos.style.width = (anchoDinamico + 50) + '%';

btn_prev.addEventListener('click',()=>{
    const cont_fotos = document.querySelector('.cont-fotos');
    if(contador_movimiento < (numImagenes * 0)){
        contador_movimiento += (100 / numImagenes);
        cont_fotos.style.transform = `translateX(${contador_movimiento}%)`;
    }
})

btn_sig.addEventListener('click',()=>{
    const cont_fotos = document.querySelector('.cont-fotos');
    if(contador_movimiento > -100 + (100/ numImagenes)){
        contador_movimiento -= (100 / numImagenes);
        cont_fotos.style.transform = `translateX(${contador_movimiento}%)`;
    }
})


