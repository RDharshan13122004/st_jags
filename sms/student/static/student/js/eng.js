// Auto-Highlight Animation
const highlights = document.querySelectorAll('.highlight-card');
let currentHighlight = 0;

function cycleHighlights() {
    highlights.forEach((card, index) => {
        card.style.opacity = index === currentHighlight ? '1' : '0.5';
        card.style.transform = index === currentHighlight ? 'scale(1.1)' : 'scale(1)';
    });

    currentHighlight = (currentHighlight + 1) % highlights.length;
}

setInterval(cycleHighlights, 2000);

// Optional: Smooth Entry Animation
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
