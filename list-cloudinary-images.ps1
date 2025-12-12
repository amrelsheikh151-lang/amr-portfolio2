# Get all images from Cloudinary root
$cloudName = "dwib2lgzp"
$apiKey = "868152855977815"
$apiSecret = "gRymDRDGDjPQ07iYrEkJdMRoodQ"

$pair = "$($apiKey):$($apiSecret)"
$encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($pair))
$headers = @{Authorization = "Basic $encodedCreds" }

Write-Host "Fetching all images from Cloudinary..." -ForegroundColor Cyan

$url = "https://api.cloudinary.com/v1_1/$cloudName/resources/image?max_results=500"
$response = Invoke-RestMethod -Uri $url -Headers $headers -Method Get

Write-Host "Total images: $($response.resources.Count)" -ForegroundColor Yellow

# Filter out samples and show first 50 project images
$projectImages = $response.resources | Where-Object { $_.public_id -notlike "samples/*" } | Select-Object -First 50

Write-Host "`nFirst 50 project images:" -ForegroundColor Green
$index = 1
foreach ($img in $projectImages) {
    $url = "https://res.cloudinary.com/$cloudName/image/upload/f_auto,q_auto/$($img.public_id)"
    Write-Host "$index. $($img.public_id)" -ForegroundColor White
    Write-Host "   $url" -ForegroundColor Gray
    $index++
}

# Save all to file
$projectImages | Select-Object public_id, format, width, height, bytes | ConvertTo-Json | Out-File "cloudinary-images-list.json" -Encoding UTF8

Write-Host "`nSaved to cloudinary-images-list.json" -ForegroundColor Green
Write-Host "Total project images: $($projectImages.Count)" -ForegroundColor Yellow
