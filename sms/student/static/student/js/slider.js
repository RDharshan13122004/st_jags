const heroSection = document.querySelector('.hero');
const images = window.heroImages;


let currentIndex = 0;

// Set initial background
heroSection.style.backgroundImage = `url('${images[currentIndex]}')`;

function changeBackground() {
    heroSection.classList.add('fade');
    setTimeout(() => {
        currentIndex = (currentIndex + 1) % images.length;
        heroSection.style.backgroundImage = `url('${images[currentIndex]}')`;
        heroSection.classList.remove('fade');
    }, 1000);
}

setInterval(changeBackground, 5000);


