const gallerySlider = document.getElementById('gallerySlider');
let scrollAmount = 0;

function autoScroll() {
    scrollAmount += 1;
    if (scrollAmount >= gallerySlider.scrollWidth - gallerySlider.clientWidth) {
        scrollAmount = 0;
    }
    gallerySlider.scrollTo({
        left: scrollAmount,
        behavior: 'smooth'
    });
}

setInterval(autoScroll, 30);
