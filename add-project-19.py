# Add Project 19: Viral2
import re

project_num = 19
project_name = "Viral2"
category = "campaign"
category_name = "Marketing Campaign"
description = "Complete project for Viral2."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472933/imgi_305_7d8f38206677425.66d05a04ca5b4_tjjmxq.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472938/imgi_304_b2b059206677425.66d05a04c9b68_z2venx.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472957/imgi_306_24c73e206677425.66d05a04ca161_knbdz5.png"
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

# Update project-19.html
with open(r'd:\website amr\amr portfolio\projects\project-19.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('Viral', project_name)
project_content = project_content.replace('Marketing Design', category_name)
project_content = project_content.replace('Complete marketing design for Viral.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 22):
    old_img = f'../images/projects/project-19/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Viral - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-19.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
