// Gallery Lightbox Functionality
document.addEventListener('DOMContentLoaded', function () {
    // Create lightbox HTML
    const lightbox = document.createElement('div');
    lightbox.className = 'lightbox';
    lightbox.innerHTML = `
        <div class="lightbox-content">
            <button class="lightbox-close">&times;</button>
            <button class="lightbox-nav lightbox-prev"><i class="fas fa-chevron-left"></i></button>
            <img src="" alt="">
            <button class="lightbox-nav lightbox-next"><i class="fas fa-chevron-right"></i></button>
        </div>
    `;
    document.body.appendChild(lightbox);

    const lightboxImg = lightbox.querySelector('img');
    const closeBtn = lightbox.querySelector('.lightbox-close');
    const prevBtn = lightbox.querySelector('.lightbox-prev');
    const nextBtn = lightbox.querySelector('.lightbox-next');

    const galleryItems = document.querySelectorAll('.gallery-item img');
    let currentIndex = 0;

    // Open lightbox
    function openLightbox(index) {
        currentIndex = index;
        lightboxImg.src = galleryItems[currentIndex].src;
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    // Close lightbox
    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
    }

    // Navigate to next image
    function nextImage() {
        currentIndex = (currentIndex + 1) % galleryItems.length;
        lightboxImg.src = galleryItems[currentIndex].src;
    }

    // Navigate to previous image
    function prevImage() {
        currentIndex = (currentIndex - 1 + galleryItems.length) % galleryItems.length;
        lightboxImg.src = galleryItems[currentIndex].src;
    }

    // Add click events to gallery items
    galleryItems.forEach((img, index) => {
        img.parentElement.addEventListener('click', () => openLightbox(index));
    });

    // Close button
    closeBtn.addEventListener('click', closeLightbox);

    // Navigation buttons
    nextBtn.addEventListener('click', nextImage);
    prevBtn.addEventListener('click', prevImage);

    // Close on background click
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (!lightbox.classList.contains('active')) return;

        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowRight') nextImage();
        if (e.key === 'ArrowLeft') prevImage();
    });
});
