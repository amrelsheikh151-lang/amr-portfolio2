# Create HTML pages for all 20 projects

$projects = @(
    @{id = 1; name = "ALOMDa Home Design"; category = "Brand Identity"; desc = "Complete brand identity design for ALOMDa Home Design based in UAE."; year = "2024"; tools = "Photoshop, Illustrator"; images = 21 },
    @{id = 2; name = "Bulgarian Company"; category = "Marketing Campaign"; desc = "Marketing campaign design for Bulgarian company with modern approach."; year = "2024"; tools = "Photoshop, Illustrator"; images = 8 },
    @{id = 3; name = "Vemo Products for Poultry"; category = "Product Design"; desc = "Product design and marketing materials for Vemo poultry products."; year = "2024"; tools = "Photoshop, Illustrator"; images = 4 },
    @{id = 4; name = "Elhamamy Difference Campaign"; category = "Marketing Campaign"; desc = "Difference campaign for Elhamamy with creative visual solutions."; year = "2024"; tools = "Photoshop"; images = 8 },
    @{id = 5; name = "Elmazraa Natural Health"; category = "Health Campaign"; desc = "Natural health campaign for Elmazraa Company."; year = "2024"; tools = "Photoshop, Illustrator"; images = 6 },
    @{id = 6; name = "Elrawda Campaign"; category = "Marketing Design"; desc = "Marketing campaign design for Elrawda."; year = "2024"; tools = "Photoshop"; images = 4 },
    @{id = 7; name = "Free Vet Magic Solution"; category = "Product Campaign"; desc = "Magic Solution campaign for Free Vet products."; year = "2024"; tools = "Photoshop, Illustrator"; images = 5 },
    @{id = 8; name = "Free Vet Nutrition"; category = "Nutrition Campaign"; desc = "Nutrition campaign for Free Vet with health focus."; year = "2024"; tools = "Photoshop"; images = 4 },
    @{id = 9; name = "German Gladiator Poultry"; category = "Product Design"; desc = "Product design for German Gladiator Poultry."; year = "2024"; tools = "Photoshop, Illustrator"; images = 3 },
    @{id = 10; name = "German Company Product"; category = "Product Design"; desc = "Professional product design for German company."; year = "2024"; tools = "Photoshop, Illustrator"; images = 3 },
    @{id = 11; name = "Italian Company Campaign"; category = "Marketing Design"; desc = "Marketing campaign for Italian company."; year = "2024"; tools = "Photoshop, Illustrator"; images = 4 },
    @{id = 12; name = "Nour AL-Islam"; category = "Brand Design"; desc = "Brand design project for Nour AL-Islam."; year = "2024"; tools = "Photoshop, Illustrator"; images = 6 },
    @{id = 13; name = "Printing"; category = "Print Design"; desc = "Collection of professional print design work and materials."; year = "2023"; tools = "Photoshop, Illustrator"; images = 27 },
    @{id = 14; name = "Ramadan Series"; category = "Motion Graphics"; desc = "Motion graphics series for Ramadan with cultural themes."; year = "2024"; tools = "After Effects, Photoshop"; images = 8 },
    @{id = 15; name = "Rawda Campaign"; category = "Marketing Design"; desc = "Marketing campaign design for Rawda."; year = "2024"; tools = "Photoshop"; images = 4 },
    @{id = 16; name = "Royal Poultry Campaign"; category = "Feed Campaign"; desc = "Campaign for Royal Poultry German Feed Company."; year = "2024"; tools = "Photoshop, Illustrator"; images = 4 },
    @{id = 17; name = "Sea Air Logistics"; category = "Brand Design"; desc = "Brand design for Sea Air Logistics Company."; year = "2023"; tools = "Illustrator, Photoshop"; images = 5 },
    @{id = 18; name = "Tanbool Come Back"; category = "Marketing Campaign"; desc = "Come Back campaign for Tanbool brand."; year = "2024"; tools = "Photoshop"; images = 4 },
    @{id = 19; name = "Viral Campaign"; category = "Social Media"; desc = "Viral social media campaign with creative concepts."; year = "2024"; tools = "Photoshop"; images = 3 },
    @{id = 20; name = "Viral Campaign 2"; category = "Social Media"; desc = "Second viral social media campaign series."; year = "2024"; tools = "Photoshop"; images = 3 }
)

foreach ($project in $projects) {
    $id = $project.id
    $title = $project.name
    $category = $project.category
    $desc = $project.desc
    $year = $project.year
    $tools = $project.tools
    $imageCount = $project.images
    
    # Determine next and previous project IDs
    $prevId = if ($id -eq 1) { 20 } else { $id - 1 }
    $nextId = if ($id -eq 20) { 1 } else { $id + 1 }
    
    # Build gallery images HTML
    $galleryHTML = ""
    for ($i = 1; $i -le $imageCount; $i++) {
        $galleryHTML += @"
            <div class="gallery-item">
                <img src="../images/projects/project-$id/img$i.jpg" alt="$title - Image $i" loading="lazy">
            </div>

"@
    }
    
    $html = @"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$title - Amr Elsheikh</title>
    <link rel="stylesheet" href="project-style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Back to Portfolio -->
    <a href="../index.html#work" class="back-link">
        <i class="fas fa-arrow-left"></i> Back to Portfolio
    </a>

    <!-- Project Hero -->
    <section class="project-hero">
        <div class="hero-content">
            <span class="project-category">$category</span>
            <h1 class="project-title">$title</h1>
            <p class="project-description">$desc</p>
            <div class="project-meta">
                <span><i class="fas fa-calendar"></i> $year</span>
                <span><i class="fas fa-tools"></i> $tools</span>
                <span><i class="fas fa-images"></i> $imageCount Images</span>
            </div>
        </div>
    </section>

    <!-- Project Gallery -->
    <section class="project-gallery">
        <div class="gallery-grid">
$galleryHTML        </div>
    </section>

    <!-- Project Navigation -->
    <section class="project-navigation">
        <a href="project-$prevId.html" class="nav-project prev">
            <i class="fas fa-arrow-left"></i>
            <span>Previous Project</span>
        </a>
        <a href="project-$nextId.html" class="nav-project next">
            <span>Next Project</span>
            <i class="fas fa-arrow-right"></i>
        </a>
    </section>

    <!-- Footer -->
    <footer class="project-footer">
        <p>&copy; 2024 Amr Elsheikh. All rights reserved.</p>
    </footer>
</body>
</html>
"@
    
    $html | Out-File -FilePath "d:\amr portfolio\projects\project-$id.html" -Encoding UTF8
    Write-Host "Created project-$id.html - $title"
}

Write-Host "`n✅ All 20 project pages created successfully!"
