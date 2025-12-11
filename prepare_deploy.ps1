# Copy all necessary files for deployment

# Create deploy directory
$deployDir = "d:\amr portfolio\deploy"

# Files and folders to copy
$itemsToCopy = @(
    "index.html",
    "style.css",
    "mobile.css",
    "script.js",
    "images",
    "projects"
)

Write-Host "Copying files to deploy folder..." -ForegroundColor Cyan

foreach ($item in $itemsToCopy) {
    $source = "d:\amr portfolio\$item"
    $dest = "$deployDir\$item"
    
    if (Test-Path $source) {
        if (Test-Path $source -PathType Container) {
            # It's a directory
            Copy-Item -Path $source -Destination $dest -Recurse -Force
            Write-Host "  ✓ Copied folder: $item" -ForegroundColor Green
        }
        else {
            # It's a file
            Copy-Item -Path $source -Destination $dest -Force
            Write-Host "  ✓ Copied file: $item" -ForegroundColor Green
        }
    }
    else {
        Write-Host "  ⚠ Not found: $item" -ForegroundColor Yellow
    }
}

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "✅ Deployment package ready!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "`nLocation: $deployDir" -ForegroundColor Cyan
Write-Host "`nNext steps:" -ForegroundColor Yellow
Write-Host "1. Go to https://app.netlify.com/drop" -ForegroundColor White
Write-Host "2. Drag the 'deploy' folder to the upload area" -ForegroundColor White
Write-Host "3. Your site will be live in seconds!" -ForegroundColor White
