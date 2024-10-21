document.addEventListener("DOMContentLoaded", function () {
    function scrollCarousel(direction) {
        const carousel = document.getElementById('carousel');
        if (!carousel) {
            console.error("Elemento carousel não encontrado.");
            return;
        }
        const scrollAmount = 300; // Ajuste conforme a largura dos itens
        carousel.scrollBy({
            left: direction * scrollAmount,
            behavior: 'smooth'
        });
    }

    window.scrollCarousel = scrollCarousel;
});





// Para o movimento usando o clique/arrastar ------------------------------------------------------------------
const carousel = document.getElementById('carousel');

let isDragging = false;
let startX;
let scrollLeft;

carousel.addEventListener('mousedown', (e) => {
    isDragging = true;
    carousel.classList.add('dragging');
    startX = e.pageX - carousel.offsetLeft;
    scrollLeft = carousel.scrollLeft;
    e.preventDefault(); // Evita seleção de texto enquanto arrasta
});

carousel.addEventListener('mouseleave', () => {
    isDragging = false;
    carousel.classList.remove('dragging');
});

carousel.addEventListener('mouseup', () => {
    isDragging = false;
    carousel.classList.remove('dragging');
});

carousel.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    e.preventDefault();
    const x = e.pageX - carousel.offsetLeft;
    const walk = (x - startX) * 2; // Multiplicador para ajustar a sensibilidade do arrasto
    carousel.scrollLeft = scrollLeft - walk;
});

// Para dispositivos de toque (mobile) --------------------------------------------------------------------
carousel.addEventListener('touchstart', (e) => {
    isDragging = true;
    startX = e.touches[0].pageX - carousel.offsetLeft;
    scrollLeft = carousel.scrollLeft;
    e.preventDefault();
});

carousel.addEventListener('touchend', () => {
    isDragging = false;
});

carousel.addEventListener('touchmove', (e) => {
    if (!isDragging) return;
    e.preventDefault();
    const x = e.touches[0].pageX - carousel.offsetLeft;
    const walk = (x - startX) * 1.5; // Multiplicador para ajustar a sensibilidade do arrasto
    carousel.scrollLeft = scrollLeft - walk;
});
