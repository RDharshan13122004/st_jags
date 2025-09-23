// Auto Animate Specializations
const specCards = document.querySelectorAll('.spec-card');
let currentSpec = 0;

function highlightSpecialization() {
    specCards.forEach((card, index) => {
        card.style.opacity = index === currentSpec ? '1' : '0.7';
        card.style.transform = index === currentSpec ? 'scale(1.1)' : 'scale(1)';
    });
    currentSpec = (currentSpec + 1) % specCards.length;
}

setInterval(highlightSpecialization, 2000);

// Smooth Entry for Faculty Cards
window.addEventListener('scroll', () => {
    document.querySelectorAll('.faculty-card').forEach(card => {
        const cardPosition = card.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.2;
        if (cardPosition < screenPosition) {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }
    });
});
