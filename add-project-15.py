# Add Project 15: Rawda 2
import re

project_num = 15
project_name = "Rawda 2"
category = "campaign"
category_name = "Marketing Campaign"
description = "Complete project for Rawda 2."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472830/imgi_292_f3376d206676407.66d0578be0411_nanqqj.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472836/imgi_293_612049206676407.66d0578be0bb4_uiwnpj.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472857/imgi_297_cfcc3e206676407.66d0578bdf41b_g661ha.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472864/imgi_295_e94921206676407.66d0578bdfc64_efuww0.png"
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

# Update project-15.html
with open(r'd:\website amr\amr portfolio\projects\project-15.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('Rawda Campaign', project_name)
project_content = project_content.replace('Marketing Design', category_name)
project_content = project_content.replace('Complete marketing design for Rawda Campaign.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 22):
    old_img = f'../images/projects/project-15/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Rawda Campaign - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-15.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
