// Optimize image loading for mobile
document.addEventListener('DOMContentLoaded', function () {
    // Add Intersection Observer for lazy loading
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;

                // Get original src
                const originalSrc = img.src;

                // Check if it's a Cloudinary URL
                if (originalSrc.includes('cloudinary.com')) {
                    // Add mobile optimizations to Cloudinary URL
                    let optimizedSrc = originalSrc;

                    // Check if on mobile
                    if (window.innerWidth <= 768) {
                        // Insert transformations before the version number
                        optimizedSrc = originalSrc.replace(
                            '/upload/',
                            '/upload/f_auto,q_auto,w_800,c_limit/'
                        );
                    } else {
                        // Desktop - still optimize but larger
                        optimizedSrc = originalSrc.replace(
                            '/upload/',
                            '/upload/f_auto,q_auto,w_1200,c_limit/'
                        );
                    }

                    // Load optimized image
                    img.src = optimizedSrc;
                }

                // Add loaded class for fade-in effect
                img.onload = function () {
                    img.classList.add('loaded');
                };

                observer.unobserve(img);
            }
        });
    }, {
        rootMargin: '50px' // Start loading 50px before image enters viewport
    });

    // Observe all project images
    const projectImages = document.querySAll('.project-bg-img');
    projectImages.forEach(img => {
        // Add loading class
        img.classList.add('loading');
        imageObserver.observe(img);
    });
});
