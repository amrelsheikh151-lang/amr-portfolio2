# Update all project pages to 2025

$projectFiles = Get-ChildItem "d:\amr portfolio\projects\project-*.html"

foreach ($file in $projectFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    # Replace 2024 with 2025
    $content = $content -replace '2024', '2025'
    
    $content | Out-File -FilePath $file.FullName -Encoding UTF8 -NoNewline
    Write-Host "Updated $($file.Name)" -ForegroundColor Green
}

Write-Host "`n✅ All project pages updated to 2025!" -ForegroundColor Green
