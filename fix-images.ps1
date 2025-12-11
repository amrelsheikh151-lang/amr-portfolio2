# Quick Fix Script - Convert background-image to img tags
$htmlFile = "d:\website amr\amr portfolio\index.html"
$content = Get-Content $htmlFile -Raw

# Replace background-image divs with img tags
$content = $content -replace '<div class="project-image"\s+style="background-image: url\(''([^'']+)''\); background-size: cover; background-position: center;">',
'<div class="project-image"><img src="$1" alt="Project" class="project-bg-img" loading="lazy">'

# Save
$content | Set-Content $htmlFile -NoNewline

Write-Host "Converted background-images to img tags!" -ForegroundColor Green
