// EXTREME Mobile Optimization - INSTANT Loading
// Smallest possible images while maintaining acceptable quality
(function () {
    'use strict';

    const isMobile = window.innerWidth <= 768;

    if (!isMobile) {
        return; // Desktop unchanged
    }

    console.log('📱 EXTREME mobile optimization');

    function optimizeImages() {
        const projectImages = document.querySelectorAll('.project-bg-img');

        projectImages.forEach((img, index) => {
            const originalSrc = img.src;

            if (!originalSrc.includes('cloudinary.com')) {
                return;
            }

            // ULTRA TINY blur (15px, ~1KB - loads INSTANTLY)
            const tinyBlurSrc = originalSrc.replace(
                '/upload/',
                '/upload/w_15,q_5,e_blur:2000/'
            );

            // EXTREME mobile optimization
            // Very small (250px), low quality (30%), WebP format
            const mobileSrc = originalSrc.replace(
                '/upload/',
                '/upload/f_webp,q_30,w_250,c_limit/'
            );

            // Set ultra tiny blur IMMEDIATELY
            img.src = tinyBlurSrc;
            img.style.filter = 'blur(30px)';
            img.style.transform = 'scale(1.2)';
            img.classList.add('blur-up');

            // Load full image only when visible
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const fullImg = new Image();
                        fullImg.onload = function () {
                            img.src = mobileSrc;
                            img.style.filter = 'blur(0)';
                            img.style.transform = 'scale(1)';
                            img.classList.remove('blur-up');
                            img.classList.add('loaded');
                        };
                        fullImg.src = mobileSrc;
                        observer.unobserve(entry.target);
                    }
                });
            }, {
                rootMargin: '150px'
            });

            observer.observe(img);
        });

        console.log(`⚡ ${projectImages.length} images ultra-optimized!`);
    }

    // Run immediately
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', optimizeImages);
    } else {
        optimizeImages();
    }
})();
