let contador_moviemiento = 0;

const btn_prev = document.querySelector('.btn-flecha-izq');
btn_prev.addEventListener('click',()=>{
    const cont_fotos = document.getElementById('cont-fotos');
    
    if(contador_moviemiento < 200){
        contador_moviemiento += 100;

        cont_fotos.style.transform = `translateX(-${contador_movimiento})`;
    }
})
