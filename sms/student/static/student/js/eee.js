// Auto Sliding Courses
let slider = document.getElementById('courseSlider');
let isDragging = false;
let startX;
let scrollLeft;

function autoSlide() {
    slider.scrollBy({ left: 1, behavior: 'smooth' });
    if (slider.scrollLeft + slider.offsetWidth >= slider.scrollWidth) {
        slider.scrollTo({ left: 0, behavior: 'smooth' });
    }
}
setInterval(autoSlide, 30); // Smooth continuous scroll

// Optional: Drag to scroll manually
slider.addEventListener('mousedown', (e) => {
    isDragging = true;
    startX = e.pageX - slider.offsetLeft;
    scrollLeft = slider.scrollLeft;
});

slider.addEventListener('mouseleave', () => { isDragging = false; });
slider.addEventListener('mouseup', () => { isDragging = false; });

slider.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    e.preventDefault();
    const x = e.pageX - slider.offsetLeft;
    const walk = (x - startX) * 2;
    slider.scrollLeft = scrollLeft - walk;
});
