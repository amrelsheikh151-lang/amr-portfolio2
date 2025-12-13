# Add Project 4: Bulgarian company, vemo products for poultry
import re

# Project 4 data
project_num = 4
project_name = "Bulgarian company, vemo products for poultry"
category = "campaign"
category_name = "Marketing Campaign"
description = "Complete project for Bulgarian company, vemo products for poultry."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472180/imgi_305_2e63ae206398315.66cc3d9c97856_pqoweu.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472190/imgi_307_786ff5206398315.66cc3d9c96a0e_s237qe.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472169/imgi_311_8b4372206398315.66cc3ef13807c_zee7ht.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472168/imgi_309_d01cd9206398315.66cc3d9c971d6_erhx2e.jpg"
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

# 2. Update project-4.html
with open(r'd:\website amr\amr portfolio\projects\project-4.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

# Update title and meta
project_content = project_content.replace('Elhamamy Difference Campaign', project_name)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)
project_content = project_content.replace('Complete marketing campaign for Elhamamy Difference Campaign.', description)

# Replace gallery images
for i in range(1, 22):
    old_img = f'../images/projects/project-4/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Elhamamy Difference Campaign - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-4.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name}")
print(f"Gallery: {len(images)} images")
