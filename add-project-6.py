# Add Project 6: Elmazraa Company Natural Health Campaign
import re

project_num = 6
project_name = "Elmazraa Company Natural Health Campaign"
category = "health"
category_name = "Health Campaign"
description = "Complete project for Elmazraa Company Natural Health Campaign."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472371/imgi_307_dee6e8206670303.66d0460c6377b_nado0u.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472368/imgi_310_2ed110206670303.66d0460c63f9b_zp1imt.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472352/imgi_312_825e0c206670303.66d0460c64da8_jz360j.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472350/imgi_308_fc01f2206670303.66d0460c64928_izpbjo.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472346/imgi_311_b5f698206670303.66d0460c64449_bbpton.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472340/imgi_309_86260f206670303.66d0460c6550f_frhod9.png"
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

# Update project-6.html
with open(r'd:\website amr\amr portfolio\projects\project-6.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('Elrawda Campaign', project_name)
project_content = project_content.replace('Marketing Design', category_name)
project_content = project_content.replace('Complete marketing design for Elrawda Campaign.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 22):
    old_img = f'../images/projects/project-6/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Elrawda Campaign - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-6.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
