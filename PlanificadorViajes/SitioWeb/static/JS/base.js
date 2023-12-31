const btn_menu = document.querySelector('.menu');
btn_menu.addEventListener('click', ()=>{
    openSidebar();
})

function closeSidebar(){
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.remove('show-sidebar');
    const links = document.querySelector('.cont-links');
    links.classList.remove('show');
    const titulo = document.querySelector('.titulo');
    titulo.classList.remove('show');
    const login = document.querySelector('.cont-login');
    login.classList.remove('show');
    btn_menu.classList.remove('rotate-menu');
    const main = document.querySelector('main');
    main.classList.remove('background-off');
}

function openSidebar(){
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('show-sidebar');
    const links = document.querySelector('.cont-links');
    links.classList.toggle('show');
    const titulo = document.querySelector('.titulo');
    titulo.classList.toggle('show');
    const login = document.querySelector('.cont-login');
    login.classList.toggle('show');
    btn_menu.classList.toggle('rotate-menu');
    const main = document.querySelector('main');
    main.classList.toggle('background-off');
}