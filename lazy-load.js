// Enhanced Lazy Loading for Background Images
(function() {
    'use strict';

    // Configuration
    const config = {
        rootMargin: '50px', // Start loading 50px before element enters viewport
        threshold: 0.01
    };

    // Lazy load background images
    function lazyLoadBackgroundImages() {
        const imageElements = document.querySelectorAll('.project-image[style*="background-image"]');
        
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const element = entry.target;
                        
                        // Get the background image URL from inline style
                        const bgImage = element.style.backgroundImage;
                        
                        if (bgImage && bgImage !== 'none') {
                            // Extract URL from url('...')
                            const imageUrl = bgImage.match(/url\(['"]?([^'"]+)['"]?\)/);
                            
                            if (imageUrl && imageUrl[1]) {
                                // Preload the image
                                const img = new Image();
                                img.onload = () => {
                                    element.classList.add('loaded');
                                };
                                img.onerror = () => {
                                    console.warn('Failed to load image:', imageUrl[1]);
                                    element.classList.add('loaded'); // Still mark as loaded to stop shimmer
                                };
                                img.src = imageUrl[1];
                            }
                        }
                        
                        observer.unobserve(element);
                    }
                });
            }, config);

            // Observe all project images
            imageElements.forEach(img => {
                imageObserver.observe(img);
            });
        } else {
            // Fallback for browsers without IntersectionObserver
            imageElements.forEach(element => {
                element.classList.add('loaded');
            });
        }
    }

    // Lazy load regular img tags
    function lazyLoadImages() {
        const images = document.querySelectorAll('img[data-src]');
        
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        if (img.dataset.src) {
                            img.src = img.dataset.src;
                            img.classList.add('loaded');
                            img.removeAttribute('data-src');
                            observer.unobserve(img);
                        }
                    }
                });
            }, config);

            images.forEach(img => imageObserver.observe(img));
        } else {
            // Fallback
            images.forEach(img => {
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                }
            });
        }
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            lazyLoadBackgroundImages();
            lazyLoadImages();
        });
    } else {
        lazyLoadBackgroundImages();
        lazyLoadImages();
    }

    // Performance monitoring (optional, can be removed in production)
    if (window.performance && window.performance.mark) {
        window.addEventListener('load', () => {
            performance.mark('lazy-load-complete');
            console.log('Lazy loading initialized');
        });
    }
})();
