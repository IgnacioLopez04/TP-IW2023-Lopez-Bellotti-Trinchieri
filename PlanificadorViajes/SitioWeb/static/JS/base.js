const btn_menu = document.querySelector('.menu');
btn_menu.addEventListener('click', ()=>{
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('show-sidebar');
    const links = document.querySelector('.cont-links');
    links.classList.toggle('show');
    const titulo = document.querySelector('.titulo');
    titulo.classList.toggle('show');
    const login = document.querySelector('.cont-login');
    login.classList.toggle('show');
    btn_menu.classList.toggle('rotate-menu');
})