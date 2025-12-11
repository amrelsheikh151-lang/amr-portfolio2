# Quick Git Setup & Upload Script
# Run this after installing Git

Write-Host "🚀 Portfolio Upload to GitHub" -ForegroundColor Cyan
Write-Host "================================`n" -ForegroundColor Cyan

# Check if Git is installed
try {
    git --version | Out-Null
    Write-Host "✅ Git is installed!`n" -ForegroundColor Green
}
catch {
    Write-Host "❌ Git is NOT installed!" -ForegroundColor Red
    Write-Host "Please install Git first from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host "After installation, close this window and run this script again.`n" -ForegroundColor Yellow
    pause
    exit
}

# Navigate to portfolio directory
Set-Location "d:\amr portfolio"

Write-Host "📁 Current directory: $(Get-Location)`n" -ForegroundColor Yellow

# Ask for GitHub username
Write-Host "Please enter your GitHub username:" -ForegroundColor Cyan
$username = Read-Host

if ([string]::IsNullOrWhiteSpace($username)) {
    Write-Host "❌ Username cannot be empty!" -ForegroundColor Red
    pause
    exit
}

Write-Host "`n🔧 Initializing Git repository...`n" -ForegroundColor Yellow

# Initialize Git
git init

# Configure Git (if not already configured)
$gitName = git config --global user.name
if ([string]::IsNullOrWhiteSpace($gitName)) {
    Write-Host "Setting up Git user..." -ForegroundColor Yellow
    git config --global user.name "Amr Elsheikh"
    git config --global user.email "amrelsheikh151@gmail.com"
}

# Add all files
Write-Host "📦 Adding all files..." -ForegroundColor Yellow
git add .

# Commit
Write-Host "💾 Creating commit..." -ForegroundColor Yellow
git commit -m "Initial portfolio upload - Professional portfolio with chat assistant"

# Add remote
Write-Host "`n🔗 Adding GitHub remote..." -ForegroundColor Yellow
$repoUrl = "https://github.com/$username/portfolio.git"
git remote add origin $repoUrl

# Set branch to main
Write-Host "🌿 Setting main branch..." -ForegroundColor Yellow
git branch -M main

# Push to GitHub
Write-Host "`n🚀 Uploading to GitHub..." -ForegroundColor Cyan
Write-Host "You may need to enter your GitHub credentials:" -ForegroundColor Yellow
Write-Host "  Username: $username" -ForegroundColor White
Write-Host "  Password: Use Personal Access Token (NOT your password!)`n" -ForegroundColor White

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ SUCCESS! Portfolio uploaded to GitHub!" -ForegroundColor Green
    Write-Host "`n📍 Next steps:" -ForegroundColor Cyan
    Write-Host "1. Go to: https://github.com/$username/portfolio" -ForegroundColor White
    Write-Host "2. Click 'Settings' → 'Pages'" -ForegroundColor White
    Write-Host "3. Source: main branch → Save" -ForegroundColor White
    Write-Host "4. Your site will be at: https://$username.github.io/portfolio/`n" -ForegroundColor Green
    
    # Open GitHub repo
    Start-Process "https://github.com/$username/portfolio"
}
else {
    Write-Host "`n❌ Upload failed!" -ForegroundColor Red
    Write-Host "`nCommon issues:" -ForegroundColor Yellow
    Write-Host "1. Repository doesn't exist - Create it first at github.com/new" -ForegroundColor White
    Write-Host "2. Wrong credentials - Use Personal Access Token" -ForegroundColor White
    Write-Host "3. Repository name mismatch - Make sure it's called 'portfolio'`n" -ForegroundColor White
}

pause
