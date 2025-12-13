# Fix Project 9: Free Vet Nutrition Campaign - Add missing 1 image (has 3, needs 4)
import re

project_num = 9
project_name = "Free Vet Nutrition Campaign"

# All 4 images from original data
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472545/imgi_312_a4dd81206669905.66d044d8047dd_qzdp1b.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472531/imgi_307_780d33206669905.66d044d80415a_y5beex.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472509/imgi_310_a39010206669905.66d044d8055b3_b0kwfn.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472503/imgi_309_c7764e206669905.66d044d805aff_uqt4gd.png"
]

with open(r'd:\website amr\amr portfolio\projects\project-9.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'\d+ Images', f'{len(images)} Images', content)

for i in range(1, 30):
    old_img = f'../images/projects/project-9/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        content = content.replace(old_img, new_img)
        content = content.replace(f'German Gladiator Poultry - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        content = re.sub(pattern, '', content)

with open(r'd:\website amr\amr portfolio\projects\project-9.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print(f"Fixed Project {project_num}: {project_name} - {len(images)} images")
