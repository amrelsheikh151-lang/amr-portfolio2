// Mobile-ONLY Image Optimization - Desktop untouched
document.addEventListener('DOMContentLoaded', function () {
    // Only run on mobile devices
    const isMobile = window.innerWidth <= 768;

    if (!isMobile) {
        console.log('Desktop detected - skipping mobile optimizations');
        return; // Exit early on desktop
    }

    console.log('Mobile detected - applying optimizations');

    // Aggressive mobile optimization
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                const originalSrc = img.getAttribute('data-src') || img.src;

                // Only optimize Cloudinary images
                if (originalSrc.includes('cloudinary.com')) {
                    // AGGRESSIVE mobile optimization
                    const optimizedSrc = originalSrc.replace(
                        '/upload/',
                        '/upload/f_auto,q_70,w_600,c_limit,dpr_auto/'
                    );

                    console.log('Loading optimized image:', optimizedSrc);

                    // Create new image to preload
                    const tempImg = new Image();
                    tempImg.onload = function () {
                        img.src = optimizedSrc;
                        img.classList.remove('loading');
                        img.classList.add('loaded');
                    };
                    tempImg.src = optimizedSrc;
                } else {
                    img.classList.remove('loading');
                    img.classList.add('loaded');
                }

                observer.unobserve(img);
            }
        });
    }, {
        rootMargin: '100px', // Start loading earlier
        threshold: 0.01
    });

    // Find all project images
    const projectImages = document.querySelectorAll('.project-bg-img');
    console.log('Found', projectImages.length, 'project images');

    projectImages.forEach(img => {
        // Store original src
        if (!img.getAttribute('data-src')) {
            img.setAttribute('data-src', img.src);
        }

        // Add loading class
        img.classList.add('loading');

        // Clear src to prevent loading
        img.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1 1"%3E%3C/svg%3E';

        // Observe
        imageObserver.observe(img);
    });
});
