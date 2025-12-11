# Ultra-Fast Image Compression Script
Add-Type -AssemblyName System.Drawing

Write-Host "Ultra-Fast Image Compression..." -ForegroundColor Cyan

$sourceFolder = "d:\website amr\amr portfolio"
$quality = 50

$images = Get-ChildItem "$sourceFolder\images" -Recurse -Include *.jpg, *.jpeg, *.png | Where-Object { $_.Length -gt 100KB }

Write-Host "Found $($images.Count) images to compress" -ForegroundColor Yellow

$compressed = 0
$savedSpace = 0

foreach ($img in $images) {
    try {
        $originalSize = $img.Length
        $bitmap = [System.Drawing.Image]::FromFile($img.FullName)
        
        # Resize if too large
        $maxWidth = 800
        if ($bitmap.Width -gt $maxWidth) {
            $ratio = $maxWidth / $bitmap.Width
            $newHeight = [int]($bitmap.Height * $ratio)
            $newBitmap = New-Object System.Drawing.Bitmap($maxWidth, $newHeight)
            $graphics = [System.Drawing.Graphics]::FromImage($newBitmap)
            $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
            $graphics.DrawImage($bitmap, 0, 0, $maxWidth, $newHeight)
            $graphics.Dispose()
            $bitmap.Dispose()
            $bitmap = $newBitmap
        }
        
        $encoder = [System.Drawing.Imaging.Encoder]::Quality
        $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
        $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter($encoder, $quality)
        $jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
        
        $tempFile = $img.FullName + ".tmp"
        $bitmap.Save($tempFile, $jpegCodec, $encoderParams)
        $bitmap.Dispose()
        
        Remove-Item $img.FullName -Force
        Move-Item $tempFile $img.FullName -Force
        
        $newSize = (Get-Item $img.FullName).Length
        $saved = $originalSize - $newSize
        $savedSpace += $saved
        
        $reduction = [math]::Round((($originalSize - $newSize) / $originalSize) * 100, 1)
        Write-Host "Compressed $($img.Name): $([math]::Round($originalSize/1KB,0))KB -> $([math]::Round($newSize/1KB,0))KB" -ForegroundColor Green
        $compressed++
    }
    catch {
        Write-Host "Failed: $($img.Name)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Compressed $compressed images" -ForegroundColor Green
Write-Host "Saved: $([math]::Round($savedSpace/1MB,2)) MB" -ForegroundColor Cyan

$finalSize = (Get-ChildItem $sourceFolder -Recurse -File | Measure-Object -Property Length -Sum).Sum / 1MB
Write-Host "Final size: $([math]::Round($finalSize,2)) MB" -ForegroundColor Yellow
