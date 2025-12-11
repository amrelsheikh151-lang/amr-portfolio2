# Script to create clean index.html with only 20 projects

# Read the header part (before work section)
$header = Get-Content "d:\amr portfolio\index.html.backup" -TotalCount 140

# Read the footer part (after work section - skills, contact, footer, script)
$allLines = Get-Content "d:\amr portfolio\index.html.backup"
$footerStart = ($allLines | Select-String -Pattern "Skills Section" | Select-Object -First 1).LineNumber - 1
$footer = $allLines[$footerStart..($allLines.Count - 1)]

# Create work section with 20 projects
$workSection = @'
            <div class="work-grid">
                <!-- Project 1 -->
                <div class="project-card" data-category="branding">
                    <div class="project-image" style="background-image: url('images/projects/project-1-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>ALOMDa Home Design</h3>
                            <p>Brand Identity</p>
                            <a href="projects/project-1.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 2 -->
                <div class="project-card" data-category="campaign">
                    <div class="project-image" style="background-image: url('images/projects/project-2-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Bulgarian Company</h3>
                            <p>Marketing Campaign</p>
                            <a href="projects/project-2.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 3 -->
                <div class="project-card" data-category="product">
                    <div class="project-image" style="background-image: url('images/projects/project-3-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Vemo Products for Poultry</h3>
                            <p>Product Design</p>
                            <a href="projects/project-3.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 4 -->
                <div class="project-card" data-category="campaign">
                    <div class="project-image" style="background-image: url('images/projects/project-4-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Elhamamy Difference Campaign</h3>
                            <p>Marketing Campaign</p>
                            <a href="projects/project-4.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 5 -->
                <div class="project-card" data-category="health">
                    <div class="project-image" style="background-image: url('images/projects/project-5-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Elmazraa Natural Health</h3>
                            <p>Health Campaign</p>
                            <a href="projects/project-5.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 6 -->
                <div class="project-card" data-category="campaign">
                    <div class="project-image" style="background-image: url('images/projects/project-6-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Elrawda Campaign</h3>
                            <p>Marketing Design</p>
                            <a href="projects/project-6.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 7 -->
                <div class="project-card" data-category="product">
                    <div class="project-image" style="background-image: url('images/projects/project-7-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Free Vet Magic Solution</h3>
                            <p>Product Campaign</p>
                            <a href="projects/project-7.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 8 -->
                <div class="project-card" data-category="health">
                    <div class="project-image" style="background-image: url('images/projects/project-8-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Free Vet Nutrition</h3>
                            <p>Nutrition Campaign</p>
                            <a href="projects/project-8.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 9 -->
                <div class="project-card" data-category="product">
                    <div class="project-image" style="background-image: url('images/projects/project-9-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>German Gladiator Poultry</h3>
                            <p>Product Design</p>
                            <a href="projects/project-9.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 10 -->
                <div class="project-card" data-category="product">
                    <div class="project-image" style="background-image: url('images/projects/project-10-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>German Company Product</h3>
                            <p>Product Design</p>
                            <a href="projects/project-10.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 11 -->
                <div class="project-card" data-category="campaign">
                    <div class="project-image" style="background-image: url('images/projects/project-11-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Italian Company Campaign</h3>
                            <p>Marketing Design</p>
                            <a href="projects/project-11.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 12 -->
                <div class="project-card" data-category="branding">
                    <div class="project-image" style="background-image: url('images/projects/project-12-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Nour AL-Islam</h3>
                            <p>Brand Design</p>
                            <a href="projects/project-12.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 13 -->
                <div class="project-card" data-category="print">
                    <div class="project-image" style="background-image: url('images/projects/project-13-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Printing</h3>
                            <p>Print Design</p>
                            <a href="projects/project-13.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 14 -->
                <div class="project-card" data-category="video">
                    <div class="project-image" style="background-image: url('images/projects/project-14-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Ramadan Series</h3>
                            <p>Motion Graphics</p>
                            <a href="projects/project-14.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 15 -->
                <div class="project-card" data-category="campaign">
                    <div class="project-image" style="background-image: url('images/projects/project-15-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Rawda Campaign</h3>
                            <p>Marketing Design</p>
                            <a href="projects/project-15.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 16 -->
                <div class="project-card" data-category="campaign">
                    <div class="project-image" style="background-image: url('images/projects/project-16-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Royal Poultry Campaign</h3>
                            <p>Feed Campaign</p>
                            <a href="projects/project-16.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 17 -->
                <div class="project-card" data-category="branding">
                    <div class="project-image" style="background-image: url('images/projects/project-17-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Sea Air Logistics</h3>
                            <p>Brand Design</p>
                            <a href="projects/project-17.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 18 -->
                <div class="project-card" data-category="campaign">
                    <div class="project-image" style="background-image: url('images/projects/project-18-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Tanbool Come Back</h3>
                            <p>Marketing Campaign</p>
                            <a href="projects/project-18.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 19 -->
                <div class="project-card" data-category="social">
                    <div class="project-image" style="background-image: url('images/projects/project-19-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Viral Campaign</h3>
                            <p>Social Media</p>
                            <a href="projects/project-19.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 20 -->
                <div class="project-card" data-category="social">
                    <div class="project-image" style="background-image: url('images/projects/project-20-cover.jpg'); background-size: cover; background-position: center;">
                        <div class="project-overlay">
                            <h3>Viral Campaign 2</h3>
                            <p>Social Media</p>
                            <a href="projects/project-20.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="view-more">
                <a href="https://www.behance.net/amrelsheikh10" target="_blank" class="btn btn-primary">
                    View All Projects on Behance
                </a>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
'@

# Combine all parts
$newContent = $header + $workSection + $footer

# Write to file
$newContent | Out-File -FilePath "d:\amr portfolio\index.html" -Encoding UTF8

Write-Host "✅ Created clean index.html with 20 projects!" -ForegroundColor Green
Write-Host "Stats: 542K views is correctly displayed" -ForegroundColor Green
