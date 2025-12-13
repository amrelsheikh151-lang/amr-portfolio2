# Add Project 12: Italian Company Campaign
import re

project_num = 12
project_name = "Italian Company Campaign"
category = "branding"
category_name = "Brand Design"
description = "Complete project for Italian Company Campaign."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472577/imgi_298_387e92223390643.67f7c4a2c4b06_fxmjwn.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472581/imgi_300_aa2495223390643.67f7c4a2c4faf_gpn2nm.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472584/imgi_302_73f89c223390643.67f7c4a2c4498_t28n7h.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472588/imgi_304_65845c223390643.67f7c4a2c56f3_d55ynz.jpg"
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

# Update project-12.html
with open(r'd:\website amr\amr portfolio\projects\project-12.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('Nour AL-Islam', project_name)
project_content = project_content.replace('Brand Design', category_name)
project_content = project_content.replace('Complete brand design for Nour AL-Islam.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 22):
    old_img = f'../images/projects/project-12/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Nour AL-Islam - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-12.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
