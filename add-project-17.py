# Add Project 17: Tanbool Come Back Capmaign
import re

project_num = 17
project_name = "Tanbool Come Back Capmaign"
category = "campaign"
category_name = "Marketing Campaign"
description = "Complete project for Tanbool Come Back Capmaign."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472936/imgi_305_4f38a5206677067.66d059272315b_rsetbe.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472911/imgi_308_e8d3b6206677067.66d0592722ac2_ff0pub.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472909/imgi_307_fdcfc7206677067.66d059272382b_vvacsp.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472906/imgi_306_bf9014206677067.66d059272249f_nbdnra.jpg"
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

# Update project-17.html
with open(r'd:\website amr\amr portfolio\projects\project-17.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('Sea Air Logistics', project_name)
project_content = project_content.replace('Brand Design', category_name)
project_content = project_content.replace('Complete brand design for Sea Air Logistics.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 22):
    old_img = f'../images/projects/project-17/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Sea Air Logistics - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-17.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
