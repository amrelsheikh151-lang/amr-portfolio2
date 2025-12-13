# Add Project 14: Ramdan Series
import re

project_num = 14
project_name = "Ramdan Series"
category = "campaign"
category_name = "Marketing Campaign"
description = "Complete project for Ramdan Series."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472768/imgi_309_0eda93223000285.67f0f1be8246f_zy8fnu.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472753/imgi_317_dcddd6223000285.67f0f1be8080f_oq8nzv.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472749/imgi_313_961701223000285.67f0f1be7ff7c_hwfhlf.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472742/imgi_315_d2108f223000285.67f0f1be82e92_a2bphf.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472740/imgi_307_cb18eb223000285.67f0f1be82997_gqiixr.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472739/imgi_304_33a260223000285.67f0f1be81cab_zwcdu3.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472737/imgi_311_404ead223000285.67f0f1be8103a_ahv0r3.jpg"
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

# Update project-14.html
with open(r'd:\website amr\amr portfolio\projects\project-14.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('Ramadan Series', project_name)
project_content = project_content.replace('Motion Graphics', category_name)
project_content = project_content.replace('Complete motion graphics for Ramadan Series.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 22):
    old_img = f'../images/projects/project-14/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Ramadan Series - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-14.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
