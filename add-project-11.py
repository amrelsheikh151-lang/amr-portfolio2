# Add Project 11: German Copmany Product
import re

project_num = 11
project_name = "German Copmany Product"
category = "branding"
category_name = "Brand Design"
description = "Complete project for German Copmany Product."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472574/imgi_305_0a5e76233736491.68b6caec4c7fe_dteyix.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472623/imgi_303_c38f9f233736491.68b5b0b87ca3f_br35co.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472614/imgi_307_130add233736491.68b7ff214c103_eltsfy.png"
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

# Update project-11.html
with open(r'd:\website amr\amr portfolio\projects\project-11.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('Italian Company Campaign', project_name)
project_content = project_content.replace('Marketing Design', category_name)
project_content = project_content.replace('Complete marketing design for Italian Company Campaign.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 22):
    old_img = f'../images/projects/project-11/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Italian Company Campaign - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-11.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
