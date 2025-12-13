// INSTANT Mobile Loading - Professional blur-up technique
// Desktop: COMPLETELY UNTOUCHED
document.addEventListener('DOMContentLoaded', function () {
    const isMobile = window.innerWidth <= 768;

    if (!isMobile) {
        console.log('Desktop - no changes');
        return; // Exit for desktop
    }

    console.log('Mobile - Applying INSTANT blur-up loading');

    const projectImages = document.querySelectorAll('.project-bg-img');

    projectImages.forEach((img, index) => {
        const originalSrc = img.src;

        if (!originalSrc.includes('cloudinary.com')) {
            return;
        }

        // Step 1: TINY blurred placeholder (loads INSTANTLY - ~5KB)
        const tinyBlurSrc = originalSrc.replace(
            '/upload/',
            '/upload/w_50,q_30,e_blur:1000/'
        );

        // Step 2: Optimized full image for mobile
        const fullSrc = originalSrc.replace(
            '/upload/',
            '/upload/f_auto,q_65,w_500,c_limit/'
        );

        // Load tiny blur IMMEDIATELY
        img.src = tinyBlurSrc;
        img.style.filter = 'blur(10px)';
        img.style.transform = 'scale(1.1)'; // Prevent blur edges
        img.classList.add('blur-up');

        // Preload full image in background
        const fullImg = new Image();
        fullImg.onload = function () {
            // Swap to full image with smooth transition
            img.src = fullSrc;
            img.style.filter = 'blur(0)';
            img.style.transform = 'scale(1)';
            img.classList.remove('blur-up');
            img.classList.add('loaded');
        };

        // Start loading full image
        fullImg.src = fullSrc;

        console.log(`Image ${index + 1}: Loaded tiny placeholder instantly`);
    });

    console.log(`${projectImages.length} images: Instant placeholders loaded!`);
});
