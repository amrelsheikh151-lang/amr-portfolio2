# Get ACTUAL image public IDs from Cloudinary folders
$cloudName = "dwib2lgzp"
$apiKey = "868152855977815"
$apiSecret = "gRymDRDGDjPQ07iYrEkJdMRoodQ"

$pair = "$($apiKey):$($apiSecret)"
$encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($pair))
$headers = @{Authorization = "Basic $encodedCreds" }

# Folder names from API
$folders = @(
    "ALOMDa ? Home Design Brand Identity  UAE",
    "Bulgarian Company",
    "Bulgarian company , vemo products for poultry",
    "Elhamamy  Difference Campaign",
    "Elmazraa Company  Natural Health Campaign",
    "Elrawda Campaign",
    "Free Vet  Magic Solution Campaign",
    "Free Vet  Nutrition Campaign",
    "German  Gladiator Poultry",
    "German Copmany Product",
    "Italian Company Campaign",
    "Nour AL-Islam",
    "Printing",
    "Ramdan Series",
    "Rawda 2",
    "Royal Poultry Campaign ( German Feed Company )",
    "Sea Air Logistics Company",
    "Tanbool  Come Back Capmaign",
    "Viral",
    "Viral2"
)

Write-Host "Fetching ACTUAL image names from Cloudinary..." -ForegroundColor Cyan

$projectUrls = @{}
$index = 1

foreach ($folder in $folders) {
    try {
        # Get all resources in this folder
        $url = "https://api.cloudinary.com/v1_1/$cloudName/resources/image?prefix=$folder/&max_results=1"
        $response = Invoke-RestMethod -Uri $url -Headers $headers -Method Get
        
        if ($response.resources.Count -gt 0) {
            $publicId = $response.resources[0].public_id
            $cloudinaryUrl = "https://res.cloudinary.com/$cloudName/image/upload/f_auto,q_auto/$publicId"
            $projectUrls[$index] = $cloudinaryUrl
            Write-Host "Project $index`: $publicId" -ForegroundColor Green
        }
        else {
            Write-Host "Project $index`: NO IMAGES!" -ForegroundColor Red
        }
    }
    catch {
        Write-Host "Project $index`: ERROR" -ForegroundColor Red
    }
    $index++
}

# Save to JSON
$projectUrls | ConvertTo-Json | Out-File "cloudinary-urls.json" -Encoding UTF8

Write-Host "`nDONE! Found $($projectUrls.Count) project images" -ForegroundColor Green
$projectUrls.GetEnumerator() | Sort-Object Name | ForEach-Object {
    Write-Host "Project $($_.Key): $($_.Value)" -ForegroundColor Yellow
}
