# Get ALL images and filter by folder
$cloudName = "dwib2lgzp"
$apiKey = "868152855977815"
$apiSecret = "gRymDRDGDjPQ07iYrEkJdMRoodQ"

$pair = "$($apiKey):$($apiSecret)"
$encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($pair))
$headers = @{Authorization = "Basic $encodedCreds" }

Write-Host "Fetching ALL images from Cloudinary..." -ForegroundColor Cyan

# Get all images (max 500)
$url = "https://api.cloudinary.com/v1_1/$cloudName/resources/image?max_results=500"
$response = Invoke-RestMethod -Uri $url -Headers $headers -Method Get

Write-Host "Total images: $($response.resources.Count)" -ForegroundColor Yellow

# Group by folder
$folderImages = @{}
foreach ($resource in $response.resources) {
    $publicId = $resource.public_id
    
    # Skip samples folder
    if ($publicId -like "samples/*") { continue }
    
    if ($publicId -match '/') {
        $folder = $publicId.Substring(0, $publicId.LastIndexOf('/'))
        if (-not $folderImages.ContainsKey($folder)) {
            $folderImages[$folder] = @()
        }
        $folderImages[$folder] += $publicId
    }
}

Write-Host "`nProject folders found:" -ForegroundColor Green
$folderImages.GetEnumerator() | Sort-Object Name | ForEach-Object {
    Write-Host "$($_.Key): $($_.Value.Count) images" -ForegroundColor Cyan
    Write-Host "  First image: $($_.Value[0])" -ForegroundColor White
}

# Save full list
$folderImages | ConvertTo-Json -Depth 3 | Out-File "all-cloudinary-images.json" -Encoding UTF8

Write-Host "`nSaved to all-cloudinary-images.json" -ForegroundColor Green
