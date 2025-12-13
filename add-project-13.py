# Add Project 13: Nour AL-Islam
import re

project_num = 13
project_name = "Nour AL-Islam"
category = "campaign"
category_name = "Marketing Campaign"
description = "Complete project for Nour AL-Islam."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472703/imgi_308_f38da2206671831.66d04ab072c21_efrrpg.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472641/imgi_311_b37385206671831.66d04ab07520a_jdpstw.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472643/imgi_313_5ad568206671831.66d04ab07330b_m9yaxf.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472667/imgi_306_fc132d206671831.66d04ab07425f_mnye0z.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472695/imgi_310_4f2f46206671831.66d04ab074a5e_s8mwxw.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472657/imgi_312_7492f3206671831.66d04ab073ac9_uasega.png"
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

# Update project-13.html
with open(r'd:\website amr\amr portfolio\projects\project-13.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('Printing', project_name)
project_content = project_content.replace('Print Design', category_name)
project_content = project_content.replace('Complete print design for Printing.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 30):
    old_img = f'../images/projects/project-13/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Printing - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-13.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
