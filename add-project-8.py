# Add Project 8: Free Vet Magic Solution Campaign
import re

project_num = 8
project_name = "Free Vet Magic Solution Campaign"
category = "branding"
category_name = "Brand Design"
description = "Complete project for Free Vet Magic Solution Campaign."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472459/imgi_314_961396206669583.66d043d32fa57_revqjl.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472464/imgi_306_df3c86206669583.66d043d330364_o4jqne.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472482/imgi_308_ec52c9206669583.66d043d32e8ca_fvhuio.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472489/imgi_312_314fcb206669583.66d043d330c83_eavqlq.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472479/imgi_310_9e9334206669583.66d043d32f0bd_gv5icd.png"
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

# Update project-8.html
with open(r'd:\website amr\amr portfolio\projects\project-8.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('Free Vet Nutrition', project_name)
project_content = project_content.replace('Nutrition Campaign', category_name)
project_content = project_content.replace('Complete nutrition campaign for Free Vet Nutrition.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 22):
    old_img = f'../images/projects/project-8/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Free Vet Nutrition - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-8.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
