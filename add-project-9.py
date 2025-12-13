# Add Project 9: Free Vet Nutrition Campaign
import re

project_num = 9
project_name = "Free Vet Nutrition Campaign"
category = "branding"
category_name = "Brand Design"
description = "Complete project for Free Vet Nutrition Campaign."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472545/imgi_312_a4dd81206669905.66d044d8047dd_qzdp1b.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472531/imgi_307_780d33206669905.66d044d80415a_y5beex.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472509/imgi_310_a39010206669905.66d044d8055b3_b0kwfn.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472503/imgi_309_c7764e206669905.66d044d805aff_uqt4gd.png"
]

# Add to index.html
with open(r'd:\website amr\amr portfolio\index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

project_card = f'''
                <!-- Project {project_num}: {project_name} -->
                <div class="project-card" data-category="{category}">
                    <div class="project-image">
                        <img src="{images[0]}" 
                             alt="{project_name}" 
                             class="project-bg-img" 
                             loading="lazy">
                        <div class="project-overlay">
                            <h3>{project_name}</h3>
                            <p>{category_name}</p>
                            <a href="projects/project-{project_num}.html" class="project-link">
                                View Project <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>'''

index_content = index_content.replace(
    '                <!-- Projects will be added here -->',
    project_card + '\n                <!-- Projects will be added here -->'
)

with open(r'd:\website amr\amr portfolio\index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(index_content)

# Update project-9.html
with open(r'd:\website amr\amr portfolio\projects\project-9.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('German Gladiator Poultry', project_name)
project_content = project_content.replace('Product Design', category_name)
project_content = project_content.replace('Complete product design for German Gladiator Poultry.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 22):
    old_img = f'../images/projects/project-9/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'German Gladiator Poultry - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-9.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
