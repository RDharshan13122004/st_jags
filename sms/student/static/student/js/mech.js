// Section Fade-In on Scroll
const sections = document.querySelectorAll('section');

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
        }
    });
}, { threshold: 0.2 });

sections.forEach(section => {
    observer.observe(section);
});

// Typing Effect for Header
const headerTitle = document.querySelector('.mech-header h1');
const titleText = "Mechanical Engineering Department";
let charIndex = 0;

function typeTitle() {
    if (charIndex < titleText.length) {
        headerTitle.textContent += titleText.charAt(charIndex);
        charIndex++;
        setTimeout(typeTitle, 100);
    }
}

headerTitle.textContent = '';
typeTitle();

// Hover Sound Effect for Course Cards
const courseCards = document.querySelectorAll('.course-card');
const hoverSound = new Audio('hover-sound.mp3'); // Add your hover sound in project folder

courseCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
        hoverSound.currentTime = 0;
        hoverSound.play();
    });
});
