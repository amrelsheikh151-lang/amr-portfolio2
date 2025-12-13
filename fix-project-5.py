# Fix Project 5: Elhamamy Difference Campaign - Add missing 2 images (has 6, needs 8)
import re

project_num = 5
project_name = "Elhamamy Difference Campaign"

# All 8 images from original data
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472274/imgi_309_b14488206671493.66d049ae8bac0_g5ksst.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472262/imgi_321_85903c206671493.66d049ae8a1db_qbd4ax.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472237/imgi_317_81b838206671493.66d049ae8c164_wetj7m.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472283/imgi_311_e5b4d5206671493.66d049ae88c02_ndth0r.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472246/imgi_319_81cfbf206671493.66d049ae8aa64_vhbir1.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472262/imgi_318_40b4a4206671493.66d049ae8b2fa_mc9ufd.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472256/imgi_313_0ec2e5206671493.66d049ae89a64_zo5xaj.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472272/imgi_315_9a7efa206671493.66d049ae89360_l4soj4.png"
]

with open(r'd:\website amr\amr portfolio\projects\project-5.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'\d+ Images', f'{len(images)} Images', content)

for i in range(1, 30):
    old_img = f'../images/projects/project-5/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        content = content.replace(old_img, new_img)
        content = content.replace(f'Elmazraa Natural Health - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        content = re.sub(pattern, '', content)

with open(r'd:\website amr\amr portfolio\projects\project-5.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print(f"Fixed Project {project_num}: {project_name} - {len(images)} images")
