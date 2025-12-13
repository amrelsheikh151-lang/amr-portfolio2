# Fix Project 8: Free Vet Magic Solution Campaign - Add missing 1 image (has 4, needs 5)
import re

project_num = 8
project_name = "Free Vet Magic Solution Campaign"

# All 5 images from original data
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472459/imgi_314_961396206669583.66d043d32fa57_revqjl.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472464/imgi_306_df3c86206669583.66d043d330364_o4jqne.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472482/imgi_308_ec52c9206669583.66d043d32e8ca_fvhuio.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472489/imgi_312_314fcb206669583.66d043d330c83_eavqlq.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472479/imgi_310_9e9334206669583.66d043d32f0bd_gv5icd.png"
]

with open(r'd:\website amr\amr portfolio\projects\project-8.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'\d+ Images', f'{len(images)} Images', content)

for i in range(1, 30):
    old_img = f'../images/projects/project-8/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        content = content.replace(old_img, new_img)
        content = content.replace(f'Free Vet Nutrition - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        content = re.sub(pattern, '', content)

with open(r'd:\website amr\amr portfolio\projects\project-8.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print(f"Fixed Project {project_num}: {project_name} - {len(images)} images")
