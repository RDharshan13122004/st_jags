// Flip Card (Click to Flip Vision/Mission)
document.querySelectorAll('.vision-card').forEach(card => {
    card.addEventListener('click', () => {
        card.querySelector('.vision-card-inner').classList.toggle('flip');
    });
});

// Course Details Accordion
document.querySelectorAll('.course-card').forEach(card => {
    card.addEventListener('click', () => {
        let details = card.querySelector('.course-details');
        if (details.style.maxHeight) {
            details.style.maxHeight = null;
        } else {
            details.style.maxHeight = details.scrollHeight + "px";
        }
    });
});

window.addEventListener('scroll', () => {
    let offset = window.scrollY;
    document.body.style.backgroundPositionY = `${offset * 0.5}px`;
});

