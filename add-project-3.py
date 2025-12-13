# Add Project 3: Bulgarian Company
import re

# Project 3 data
project_num = 3
project_name = "Bulgarian Company"
category = "campaign"
category_name = "Marketing Campaign"
description = "Complete marketing campaign for Bulgarian Company."
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

# 1. Add to index.html
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

# 2. Update project-3.html
with open(r'd:\website amr\amr portfolio\projects\project-3.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

# Update title and meta
project_content = project_content.replace('Vemo Products for Poultry', project_name)
project_content = project_content.replace('Product Design', category_name)
project_content = project_content.replace('Complete product design for Vemo Products for Poultry.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

# Replace gallery images
for i in range(1, 22):
    old_img = f'../images/projects/project-3/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Vemo Products for Poultry - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-3.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name}")
print(f"Gallery: {len(images)} images")
