# Compress Images for GitHub Upload
Add-Type -AssemblyName System.Drawing

Write-Host "🖼️ Compressing images for GitHub..." -ForegroundColor Cyan

$sourceFolder = "d:\website amr\amr portfolio"
$quality = 70  # JPEG quality (0-100)

# Get all large images
$images = Get-ChildItem "$sourceFolder\images" -Recurse -Include *.jpg, *.jpeg, *.png | Where-Object { $_.Length -gt 500KB }

Write-Host "Found $($images.Count) large images to compress`n" -ForegroundColor Yellow

$compressed = 0
$savedSpace = 0

foreach ($img in $images) {
    try {
        $originalSize = $img.Length
        
        # Load image
        $bitmap = [System.Drawing.Image]::FromFile($img.FullName)
        
        # Create encoder parameters
        $encoder = [System.Drawing.Imaging.Encoder]::Quality
        $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
        $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter($encoder, $quality)
        
        # Get JPEG codec
        $jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
        
        # Save compressed
        $tempFile = $img.FullName + ".tmp"
        $bitmap.Save($tempFile, $jpegCodec, $encoderParams)
        $bitmap.Dispose()
        
        # Replace original
        Remove-Item $img.FullName -Force
        Move-Item $tempFile $img.FullName -Force
        
        $newSize = (Get-Item $img.FullName).Length
        $saved = $originalSize - $newSize
        $savedSpace += $saved
        
        Write-Host "✓ $($img.Name): $([math]::Round($originalSize/1MB,2))MB → $([math]::Round($newSize/1MB,2))MB" -ForegroundColor Green
        $compressed++
        
    }
    catch {
        Write-Host "✗ Failed: $($img.Name)" -ForegroundColor Red
    }
}

Write-Host "`n✅ Compressed $compressed images" -ForegroundColor Green
Write-Host "💾 Saved: $([math]::Round($savedSpace/1MB,2)) MB`n" -ForegroundColor Cyan

# Check final size
$finalSize = (Get-ChildItem $sourceFolder -Recurse -File | Measure-Object -Property Length -Sum).Sum / 1MB
Write-Host "📊 Final folder size: $([math]::Round($finalSize,2)) MB" -ForegroundColor Yellow

if ($finalSize -lt 100) {
    Write-Host "`n🎉 Ready for GitHub upload!" -ForegroundColor Green
}
else {
    Write-Host "`n⚠️ Still large. Consider using Git LFS or external image hosting." -ForegroundColor Yellow
}
