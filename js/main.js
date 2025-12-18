document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const slideCounter = document.getElementById('slideCounter');
    
    const totalSlides = slides.length;
    let currentSlideIndex = parseInt(localStorage.getItem('presentation_slide_index')) || 0;

    if (currentSlideIndex >= totalSlides || currentSlideIndex < 0) {
        currentSlideIndex = 0;
    }

    function updateSlide() {
        slides.forEach((slide, index) => {
            slide.classList.remove('active');
            if (index === currentSlideIndex) {
                slide.classList.add('active');
            }
        });

        slideCounter.innerText = `${currentSlideIndex + 1} / ${totalSlides}`;
        localStorage.setItem('presentation_slide_index', currentSlideIndex);
    }

    function nextSlide() {
        currentSlideIndex = (currentSlideIndex + 1) % totalSlides;
        updateSlide();
    }

    function prevSlide() {
        currentSlideIndex = (currentSlideIndex - 1 + totalSlides) % totalSlides;
        updateSlide();
    }

    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);

    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === ' ') {
            nextSlide();
        } else if (e.key === 'ArrowLeft') {
            prevSlide();
        }
    });

    updateSlide();
});