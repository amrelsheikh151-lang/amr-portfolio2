# Update all project HTML files to include gallery.js

$projectFiles = Get-ChildItem "d:\amr portfolio\projects\project-*.html"

foreach ($file in $projectFiles) {
    $content = Get-Content $file.FullName -Raw
    
    # Check if gallery.js is already included
    if ($content -notmatch "gallery\.js") {
        # Add script tag before closing body tag
        $content = $content -replace '</body>', '    <script src="gallery.js"></script>
</body>'
        
        $content | Out-File -FilePath $file.FullName -Encoding UTF8 -NoNewline
        Write-Host "Updated $($file.Name)" -ForegroundColor Green
    }
    else {
        Write-Host "Skipped $($file.Name) - already has gallery.js" -ForegroundColor Yellow
    }
}

Write-Host "`n✅ All project pages updated with gallery.js!" -ForegroundColor Green
