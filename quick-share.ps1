# Quick Share Portfolio
# Run this to create a shareable link instantly!

Write-Host "🚀 Portfolio Quick Share" -ForegroundColor Cyan
Write-Host "========================`n" -ForegroundColor Cyan

# Check if Python is installed
$pythonInstalled = Get-Command python -ErrorAction SilentlyContinue

if ($pythonInstalled) {
    Write-Host "✅ Python found! Starting local server..." -ForegroundColor Green
    Write-Host "`n📍 Your portfolio will be available at:" -ForegroundColor Yellow
    Write-Host "   http://localhost:8000`n" -ForegroundColor White
    
    Write-Host "🌐 To share with others:" -ForegroundColor Yellow
    Write-Host "   1. Download ngrok: https://ngrok.com/download" -ForegroundColor White
    Write-Host "   2. Run: ngrok http 8000" -ForegroundColor White
    Write-Host "   3. Share the https link!`n" -ForegroundColor White
    
    Write-Host "Press Ctrl+C to stop the server`n" -ForegroundColor Red
    
    cd "d:\amr portfolio"
    python -m http.server 8000
}
else {
    Write-Host "❌ Python not installed!" -ForegroundColor Red
    Write-Host "`n📦 Creating ZIP file instead..." -ForegroundColor Yellow
    
    $zipPath = "d:\Amr-Portfolio-$(Get-Date -Format 'yyyy-MM-dd').zip"
    
    Compress-Archive -Path "d:\amr portfolio\*" -DestinationPath $zipPath -Force
    
    Write-Host "`n✅ ZIP file created!" -ForegroundColor Green
    Write-Host "📍 Location: $zipPath" -ForegroundColor White
    Write-Host "`n💡 Share this file with others!" -ForegroundColor Yellow
    Write-Host "   They can extract and open index.html`n" -ForegroundColor White
    
    # Open folder
    explorer (Split-Path $zipPath)
}
