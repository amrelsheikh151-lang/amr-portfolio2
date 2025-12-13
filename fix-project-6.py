# Fix Project 6: Elmazraa Company Natural Health Campaign - Add missing 2 images (has 4, needs 6)
import re

project_num = 6
project_name = "Elmazraa Company Natural Health Campaign"

# All 6 images from original data
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472371/imgi_307_dee6e8206670303.66d0460c6377b_nado0u.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472368/imgi_310_2ed110206670303.66d0460c63f9b_zp1imt.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472352/imgi_312_825e0c206670303.66d0460c64da8_jz360j.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472350/imgi_308_fc01f2206670303.66d0460c64928_izpbjo.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472346/imgi_311_b5f698206670303.66d0460c64449_bbpton.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472340/imgi_309_86260f206670303.66d0460c6550f_frhod9.png"
]

with open(r'd:\website amr\amr portfolio\projects\project-6.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'\d+ Images', f'{len(images)} Images', content)

for i in range(1, 30):
    old_img = f'../images/projects/project-6/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        content = content.replace(old_img, new_img)
        content = content.replace(f'Elrawda Campaign - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        content = re.sub(pattern, '', content)

with open(r'd:\website amr\amr portfolio\projects\project-6.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print(f"Fixed Project {project_num}: {project_name} - {len(images)} images")
