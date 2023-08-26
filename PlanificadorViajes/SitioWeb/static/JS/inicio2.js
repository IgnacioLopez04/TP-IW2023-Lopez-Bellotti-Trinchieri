let contador_movimiento = 0;

const btn_prev = document.querySelector('.btn-flecha-izq');
const btn_sig = document.querySelector('.btn-flecha-der');

btn_prev.addEventListener('click',()=>{
    const cont_fotos = document.querySelector('.cont-fotos');
    if(contador_movimiento < 0){
        contador_movimiento += 100;
        cont_fotos.style.transform = `translateX(${contador_movimiento}%)`;
    }
})

btn_sig.addEventListener('click',()=>{
    const cont_fotos = document.querySelector('.cont-fotos');
    if(contador_movimiento > -200){
        contador_movimiento -= 100;
        cont_fotos.style.transform = `translateX(${contador_movimiento}%)`;
    }
})


