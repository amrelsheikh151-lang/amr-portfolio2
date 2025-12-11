// Simple and Fast Image Loading - NO LAZY LOADING
// Load all images immediately for better mobile experience
(function () {
    'use strict';

    // Just mark all project images as loaded immediately
    function loadAllImages() {
        const imageElements = document.querySelectorAll('.project-image');
        imageElements.forEach(element => {
            element.classList.add('loaded');
        });

        // Also handle regular images
        const images = document.querySelectorAll('img[data-src]');
        images.forEach(img => {
            if (img.dataset.src) {
                img.src = img.dataset.src;
                img.classList.add('loaded');
                img.removeAttribute('data-src');
            }
        });
    }

    // Initialize immediately
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadAllImages);
    } else {
        loadAllImages();
    }
})();
