# PowerShell script to create all 23 project HTML pages
$projects = @(
    @{id=1; title="Profile Design"; category="Brand Identity"; desc="A comprehensive brand identity design project showcasing modern design principles and creative visual solutions."; year="2024"; tools="Photoshop, Illustrator"},
    @{id=2; title="German Company Product"; category="Product Design"; desc="Professional product design and marketing materials for a leading German company."; year="2024"; tools="Photoshop, Illustrator"},
    @{id=3; title="ALOMDa Home Design"; category="Brand Identity"; desc="Complete brand identity design for ALOMDa Home Design based in UAE."; year="2024"; tools="Photoshop, Illustrator"},
    @{id=4; title="Liberation Day"; category="Social Media Campaign"; desc="Social media campaign celebrating Liberation Day with impactful visuals."; year="2024"; tools="Photoshop"},
    @{id=5; title="Happy Easter"; category="Social Media Design"; desc="Festive Easter social media designs with vibrant colors and creative concepts."; year="2024"; tools="Photoshop"},
    @{id=6; title="Happy Easter - Happy Labour Day"; category="Social Media Campaign"; desc="Combined celebration campaign for Easter and Labour Day."; year="2024"; tools="Photoshop"},
    @{id=7; title="Bulgarian Company"; category="Marketing Campaign"; desc="Marketing campaign design for Bulgarian company with modern approach."; year="2024"; tools="Photoshop, Illustrator"},
    @{id=8; title="Italian Company Campaign"; category="Marketing Design"; desc="Professional marketing materials for Italian company campaign."; year="2024"; tools="Photoshop, Illustrator"},
    @{id=9; title="Ramadan Series"; category="Motion Graphics"; desc="Motion graphics series for Ramadan with cultural themes."; year="2024"; tools="After Effects, Photoshop"},
    @{id=10; title="Sea Air"; category="Brand Design"; desc="Brand design project for Sea Air with maritime aesthetics."; year="2023"; tools="Illustrator, Photoshop"},
    @{id=11; title="Printing"; category="Print Design"; desc="Collection of professional print design work and materials."; year="2023"; tools="Photoshop, Illustrator"},
    @{id=12; title="Various Designs"; category="Mixed Media"; desc="Diverse collection of design work across multiple categories."; year="2023"; tools="Photoshop, Illustrator"},
    @{id=13; title="Zamalek SC"; category="Sports Branding"; desc="Sports branding and visual identity for Zamalek SC football club."; year="2023"; tools="Photoshop, Illustrator"},
    @{id=14; title="Ramadan Kareem"; category="Social Media"; desc="Ramadan Kareem social media designs with traditional elements."; year="2023"; tools="Photoshop"},
    @{id=15; title="Eid Al-Fitr"; category="Social Media Design"; desc="Eid Al-Fitr celebration designs for social media platforms."; year="2023"; tools="Photoshop"},
    @{id=16; title="Eid Al-Adha"; category="Social Media Campaign"; desc="Eid Al-Adha social media campaign with festive visuals."; year="2023"; tools="Photoshop"},
    @{id=17; title="Christmas"; category="Holiday Design"; desc="Christmas holiday designs with seasonal themes and colors."; year="2023"; tools="Photoshop"},
    @{id=18; title="New Year"; category="Social Media"; desc="New Year celebration social media designs."; year="2023"; tools="Photoshop"},
    @{id=19; title="Valentine's Day"; category="Social Media Design"; desc="Valentine's Day themed social media designs with romantic elements."; year="2023"; tools="Photoshop"},
    @{id=20; title="Mother's Day"; category="Social Media Campaign"; desc="Mother's Day social media campaign celebrating mothers."; year="2023"; tools="Photoshop"},
    @{id=21; title="Father's Day"; category="Social Media Design"; desc="Father's Day social media designs honoring fathers."; year="2023"; tools="Photoshop"},
    @{id=22; title="Logo Design"; category="Brand Identity"; desc="Collection of professional logo designs for various clients."; year="2023"; tools="Illustrator"},
    @{id=23; title="Business Card"; category="Print & Branding"; desc="Professional business card designs with creative layouts."; year="2023"; tools="Illustrator, Photoshop"}
)

foreach ($project in $projects) {
    $id = $project.id
    $title = $project.title
    $category = $project.category
    $desc = $project.desc
    $year = $project.year
    $tools = $project.tools
    
    # Determine next and previous project IDs
    $prevId = if ($id -eq 1) { 23 } else { $id - 1 }
    $nextId = if ($id -eq 23) { 1 } else { $id + 1 }
    
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
    <a href="../index.html#work" class="back-link" id="back-to-portfolio">
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
            </div>
        </div>
    </section>

    <!-- Project Gallery -->
    <section class="project-gallery">
        <div class="gallery-grid">
            <div class="gallery-item">
                <img src="../images/projects/project-$id/img1.jpg" alt="$title - Image 1" id="project-$id-img1">
            </div>
            <div class="gallery-item">
                <img src="../images/projects/project-$id/img2.jpg" alt="$title - Image 2" id="project-$id-img2">
            </div>
        </div>
    </section>

    <!-- Project Navigation -->
    <section class="project-navigation">
        <a href="project-$prevId.html" class="nav-project prev" id="prev-project-$id">
            <i class="fas fa-arrow-left"></i>
            <span>Previous Project</span>
        </a>
        <a href="project-$nextId.html" class="nav-project next" id="next-project-$id">
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
    Write-Host "Created project-$id.html"
}

Write-Host "`nAll 23 project pages created successfully!"
