# Fix Project 3: Bulgarian Company - Add missing 4 images (has 4, needs 8)
import re

project_num = 3
project_name = "Bulgarian Company"

# All 8 images from original data
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472090/imgi_310_71dbc3223890459.6800ec2b05a69_gwbsbu.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472089/imgi_306_3c864b223890459.6800ec2b042a1_ptzabv.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472091/imgi_307_3938e8223890459.6800ec2b06a4a_tiltvc.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472091/imgi_304_57d1a8223890459.6800ec2b0517e_vowv0q.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472095/imgi_312_a8dd2e223890459.6800ec2b071d2_t43ljh.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472096/imgi_313_6c9031223890459.6800ec2b04b19_qm3ec0.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472095/imgi_316_915534223890459.6800ec2b07781_pobgva.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472099/imgi_318_91304d223890459.6800ec2b0626a_kaqvet.jpg"
]

with open(r'd:\website amr\amr portfolio\projects\project-3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update image count
content = re.sub(r'\d+ Images', f'{len(images)} Images', content)

# Replace all gallery images
for i in range(1, 30):
    old_img = f'../images/projects/project-3/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        content = content.replace(old_img, new_img)
        content = content.replace(f'Vemo Products for Poultry - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        content = re.sub(pattern, '', content)

with open(r'd:\website amr\amr portfolio\projects\project-3.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print(f"Fixed Project {project_num}: {project_name} - {len(images)} images")
