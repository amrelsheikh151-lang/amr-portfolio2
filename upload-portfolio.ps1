# Upload Portfolio to GitHub
Write-Host "==================================" -ForegroundColor Cyan
Write-Host "  Upload Portfolio to GitHub" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Check if we're in a git repository
if (-not (Test-Path ".git")) {
    Write-Host "Error: Not a git repository!" -ForegroundColor Red
    exit 1
}

# Get current status
Write-Host "Current Git Status:" -ForegroundColor Yellow
git status --short
Write-Host ""

# Instructions
Write-Host "Next Steps:" -ForegroundColor Green
Write-Host "1. Go to GitHub.com and create a new repository" -ForegroundColor White
Write-Host "   - Repository name: amr-portfolio" -ForegroundColor White
Write-Host "   - Description: Professional Portfolio Website" -ForegroundColor White
Write-Host "   - Public repository" -ForegroundColor White
Write-Host "   - DO NOT initialize with README" -ForegroundColor Yellow
Write-Host ""
Write-Host "2. After creating the repository, run these commands:" -ForegroundColor White
Write-Host ""
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/amr-portfolio.git" -ForegroundColor Cyan
Write-Host "   git branch -M main" -ForegroundColor Cyan
Write-Host "   git push -u origin main" -ForegroundColor Cyan
Write-Host ""

# Ask if user wants to continue
Write-Host "Do you have a GitHub repository URL? (y/n): " -ForegroundColor Yellow -NoNewline
$response = Read-Host

if ($response -eq "y") {
    Write-Host ""
    Write-Host "Enter your GitHub repository URL: " -ForegroundColor Yellow -NoNewline
    $repoUrl = Read-Host
    
    Write-Host ""
    Write-Host "Setting up remote..." -ForegroundColor Cyan
    
    try {
        git remote add origin $repoUrl
        Write-Host "Remote added successfully!" -ForegroundColor Green
        
        Write-Host ""
        Write-Host "Renaming branch to main..." -ForegroundColor Cyan
        git branch -M main
        
        Write-Host ""
        Write-Host "Pushing to GitHub..." -ForegroundColor Cyan
        git push -u origin main
        
        Write-Host ""
        Write-Host "Success! Your portfolio is now on GitHub!" -ForegroundColor Green
        Write-Host ""
        Write-Host "To enable GitHub Pages:" -ForegroundColor Yellow
        Write-Host "1. Go to your repository on GitHub" -ForegroundColor White
        Write-Host "2. Click Settings > Pages" -ForegroundColor White
        Write-Host "3. Source: Deploy from a branch" -ForegroundColor White
        Write-Host "4. Branch: main / (root)" -ForegroundColor White
        Write-Host "5. Click Save" -ForegroundColor White
        Write-Host ""
        Write-Host "Your site will be live at:" -ForegroundColor Green
        Write-Host "https://YOUR_USERNAME.github.io/amr-portfolio/" -ForegroundColor Cyan
    }
    catch {
        Write-Host "Error: $_" -ForegroundColor Red
        Write-Host ""
        Write-Host "If remote already exists, try:" -ForegroundColor Yellow
        Write-Host "git remote set-url origin $repoUrl" -ForegroundColor Cyan
    }
}
else {
    Write-Host ""
    Write-Host "No problem! Create your GitHub repository first, then run this script again." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "==================================" -ForegroundColor Cyan
