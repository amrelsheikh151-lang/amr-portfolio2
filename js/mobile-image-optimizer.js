// ULTRA-FAST Mobile Image Loading - Instant Display
// Desktop: COMPLETELY UNTOUCHED
document.addEventListener('DOMContentLoaded', function () {
    const isMobile = window.innerWidth <= 768;

    if (!isMobile) {
        console.log('✅ Desktop - Original quality images');
        return; // Exit for desktop - no changes
    }

    console.log('📱 Mobile - Activating INSTANT image loading');

    const projectImages = document.querySelectorAll('.project-bg-img');

    projectImages.forEach((img, index) => {
        const originalSrc = img.src;

        if (!originalSrc.includes('cloudinary.com')) {
            return;
        }

        // AGGRESSIVE optimization for mobile
        // Step 1: TINY blurred placeholder (loads INSTANTLY - ~3KB)
        const tinyBlurSrc = originalSrc.replace(
            '/upload/',
            '/upload/w_30,q_20,e_blur:2000/'
        );

        // Step 2: Highly optimized image for mobile (smaller, lower quality)
        const mobileSrc = originalSrc.replace(
            '/upload/',
            '/upload/f_auto,q_50,w_400,c_limit,dpr_1.0/'
        );

        // Load tiny blur IMMEDIATELY (instant display)
        img.src = tinyBlurSrc;
        img.style.filter = 'blur(20px)';
        img.style.transform = 'scale(1.1)';
        img.classList.add('blur-up');
        img.loading = 'lazy'; // Native lazy loading

        // Preload optimized image in background
        const optimizedImg = new Image();
        optimizedImg.onload = function () {
            // Swap to optimized image with smooth transition
            img.src = mobileSrc;
            img.style.filter = 'blur(0)';
            img.style.transform = 'scale(1)';
            img.classList.remove('blur-up');
            img.classList.add('loaded');
        };

        // Only load when near viewport (Intersection Observer)
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    optimizedImg.src = mobileSrc;
                    imageObserver.unobserve(entry.target);
                }
            });
        }, {
            rootMargin: '50px' // Start loading 50px before visible
        });

        imageObserver.observe(img);

        console.log(`📸 Image ${index + 1}: Instant placeholder loaded`);
    });

    console.log(`⚡ ${projectImages.length} images optimized for mobile!`);
});
