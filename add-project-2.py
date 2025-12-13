# Add Project 2: ALOMDa Home Design
import re

# Project 2 data
project_num = 2
project_name = "ALOMDa – Home Design Brand Identity UAE"
category = "branding"
category_name = "Brand Identity"
description = "Complete brand identity design for ALOMDa Home Design based in UAE."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765471448/1_2_yeizji.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765471458/2_2_m6iy10.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765471464/4_hdjxna.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765471644/9_kxz78e.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765471626/13_rvqoia.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765471684/17_cxut9l.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765471723/16_c0glqp.png"
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

# Add before "Projects will be added here" comment
index_content = index_content.replace(
    '                <!-- Projects will be added here -->',
    project_card + '\n                <!-- Projects will be added here -->'
)

with open(r'd:\website amr\amr portfolio\index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(index_content)

# 2. Update project-2.html
with open(r'd:\website amr\amr portfolio\projects\project-2.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

# Update title and meta
project_content = project_content.replace('Bulgarian Company', project_name)
project_content = project_content.replace('Marketing Campaign', category_name)
project_content = project_content.replace('Complete marketing campaign for Bulgarian Company.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

# Replace gallery images
for i in range(1, 22):
    old_img = f'../images/projects/project-2/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Bulgarian Company - Image {i}', f'{project_name} - Image {i}')
    else:
        # Remove extra gallery items
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-2.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"✅ Project {project_num} added: {project_name}")
print(f"   Cover: {images[0][:60]}...")
print(f"   Gallery: {len(images)} images")
