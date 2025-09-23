// Slider Logic
let sliderIndex = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('#slider img');
    if (index >= slides.length) sliderIndex = 0;
    else if (index < 0) sliderIndex = slides.length - 1;
    else sliderIndex = index;

    const slider = document.getElementById('slider');
    slider.style.transform = `translateX(-${sliderIndex * 100}%)`;
}

function nextSlide() { showSlide(sliderIndex + 1); }
function prevSlide() { showSlide(sliderIndex - 1); }

setInterval(nextSlide, 5000);


function shuffleHighlights() {
    const list = document.getElementById('highlightList');
    const items = Array.from(list.children);

    // Shuffle the items
    for (let i = items.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [items[i], items[j]] = [items[j], items[i]];
    }

    // Apply random background colors and reorder the list
    list.innerHTML = '';
    items.forEach(item => {
        item.style.backgroundColor = getRandomColor();
        list.appendChild(item);
    });
}

function getRandomColor() {
    const colors = ['#FF6B6B', '#6BCB77', '#4D96FF', '#FFD93D', '#A66DD4', '#FF9671', '#00C49A'];
    return colors[Math.floor(Math.random() * colors.length)];
}

// Run automatically every 4 seconds
setInterval(shuffleHighlights, 4000);

// Run once on load
shuffleHighlights();


