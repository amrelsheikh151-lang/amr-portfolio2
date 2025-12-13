// Mobile-ONLY: INSTANT loading - NO lazy loading
// Desktop: Completely untouched
document.addEventListener('DOMContentLoaded', function () {
    const isMobile = window.innerWidth <= 768;

    if (!isMobile) {
        return; // Desktop - do nothing
    }

    console.log('Mobile: Loading all images instantly with optimization');

    // Get all project images
    const projectImages = document.querySelectorAll('.project-bg-img');

    projectImages.forEach((img, index) => {
        const originalSrc = img.src;

        if (originalSrc.includes('cloudinary.com')) {
            // VERY aggressive optimization for instant mobile loading
            // Smaller size, lower quality, WebP format
            const optimizedSrc = originalSrc.replace(
                '/upload/',
                '/upload/f_auto,q_60,w_500,c_limit,dpr_auto,fl_progressive/'
            );

            // Load immediately - no lazy loading
            img.src = optimizedSrc;
            img.loading = 'eager'; // Force eager loading

            console.log(`Image ${index + 1}: ${optimizedSrc}`);
        }
    });

    console.log(`Loaded ${projectImages.length} images instantly`);
});
