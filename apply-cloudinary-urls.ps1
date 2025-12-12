# Apply Cloudinary URLs using the images we found
$indexPath = "d:\website amr\amr portfolio\index.html"
$content = Get-Content $indexPath -Raw -Encoding UTF8
$cloudName = "dwib2lgzp"

# Use the numbered images and some of the imgi_ images for first 20 projects
# Based on the list we got from Cloudinary
$projectImages = @(
    "1_2_c27vua",  # Project 1
    "2_3_zsxaaz",  # Project 2
    "3_3_iextgg",  # Project 3
    "4_3_hev27p",  # Project 4
    "imgi_300_bf3b25224301985.6808c07c291e1_g6gn4y",  # Project 5
    "imgi_306_24c73e206677425.66d05a04ca161_knbdz5",  # Project 6
    "imgi_300_42f02f224231697.6807a35227193_mr1el3",  # Project 7
    "imgi_304_b2b059206677425.66d05a04c9b68_z2venx",  # Project 8
    "imgi_305_4f38a5206677067.66d059272315b_rsetbe",  # Project 9
    "imgi_305_7d8f38206677425.66d05a04ca5b4_tjjmxq",  # Project 10
    "imgi_303_ecdb8e216147463.677ba07199710_cz9ndg",  # Project 11
    "imgi_300_8d6678224301895.6808c02e1da87_kke5ro",  # Project 12
    "imgi_310_a43591216147463.677ba07198df7_cqgols",  # Project 13
    "imgi_308_e8d3b6206677067.66d0592722ac2_ff0pub",  # Project 14
    "imgi_307_fdcfc7206677067.66d059272382b_vvacsp",  # Project 15
    "imgi_305_9f55bf216147463.677ba07199b8a_ac3d8t",  # Project 16
    "imgi_306_bf9014206677067.66d059272249f_nbdnra",  # Project 17
    "imgi_307_8a0b50216147463.677ba07199268_s8f7tk",  # Project 18
    "imgi_300_46d477216147463.677ba071988e0_qnjno5",  # Project 19
    "imgi_295_e94921206676407.66d0578bdfc64_efuww0"   # Project 20
)

Write-Host "Applying Cloudinary URLs..." -ForegroundColor Cyan

for ($i = 1; $i -le 20; $i++) {
    $oldUrl = "images/projects/project-$i-cover\.jpg"
    $newUrl = "https://res.cloudinary.com/$cloudName/image/upload/f_auto,q_auto/$($projectImages[$i-1])"
    $content = $content -replace $oldUrl, $newUrl
    Write-Host "Project $i`: $($projectImages[$i-1])" -ForegroundColor Green
}

$content | Set-Content $indexPath -Encoding UTF8 -NoNewline

Write-Host "`nDONE! All 20 projects now use Cloudinary!" -ForegroundColor Green
