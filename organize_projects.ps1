# PowerShell script to organize all projects

# Get all project folders
$projectFolders = Get-ChildItem "d:\amr portfolio\portfolio-projects" -Directory | Sort-Object Name

Write-Host "Found $($projectFolders.Count) projects" -ForegroundColor Green
Write-Host ""

$projectIndex = 1
$projectData = @()

foreach ($folder in $projectFolders) {
    $projectName = $folder.Name
    $projectPath = $folder.FullName
    
    Write-Host "Processing Project $projectIndex : $projectName" -ForegroundColor Cyan
    
    # Create project directory in images
    $imageDestDir = "d:\amr portfolio\images\projects\project-$projectIndex"
    New-Item -ItemType Directory -Path $imageDestDir -Force | Out-Null
    
    # Get all images from project folder
    $images = Get-ChildItem $projectPath -File | Where-Object { $_.Extension -match '\.(jpg|jpeg|png|gif)$' } | Sort-Object Name
    
    if ($images.Count -eq 0) {
        Write-Host "  No images found" -ForegroundColor Yellow
        $projectIndex++
        continue
    }
    
    Write-Host "  Found $($images.Count) images" -ForegroundColor Green
    
    # Copy cover image (first image)
    Copy-Item $images[0].FullName "d:\amr portfolio\images\projects\project-$projectIndex-cover.jpg" -Force
    Write-Host "  Cover: $($images[0].Name)"
    
    # Copy all images to gallery
    $imgNum = 1
    foreach ($img in $images) {
        Copy-Item $img.FullName "$imageDestDir\img$imgNum.jpg" -Force
        $imgNum++
    }
    
    Write-Host "  Copied $($images.Count) images to gallery"
    Write-Host ""
    
    # Store project info
    $projectInfo = @{
        id         = $projectIndex
        name       = $projectName
        imageCount = $images.Count
    }
    $projectData += $projectInfo
    
    $projectIndex++
}

Write-Host "========================================"
Write-Host "All projects organized successfully!" -ForegroundColor Green
Write-Host "Total projects: $($projectIndex - 1)" -ForegroundColor Green
Write-Host "========================================"
Write-Host ""

# Display project list
Write-Host "Project List:" -ForegroundColor Cyan
foreach ($proj in $projectData) {
    $id = $proj.id
    $name = $proj.name
    $count = $proj.imageCount
    Write-Host "  $id. $name - $count images"
}
