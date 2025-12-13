# Add Project 7: Elrawda Campaign
import re

project_num = 7
project_name = "Elrawda Campaign"
category = "campaign"
category_name = "Marketing Campaign"
description = "Complete project for Elrawda Campaign."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472442/imgi_306_a8a974206676069.66d0569fe0033_krrqqn.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472437/imgi_309_a1c8a2206676069.66d0569fdf212_eotk08.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472428/imgi_308_00ea87206676069.66d0569fdfaf4_rdkjn0.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472421/imgi_307_213de7206676069.66d0569fdf6c4_toxxim.png"
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

# Update project-7.html
with open(r'd:\website amr\amr portfolio\projects\project-7.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('Free Vet Magic Solution', project_name)
project_content = project_content.replace('Product Campaign', category_name)
project_content = project_content.replace('Complete product campaign for Free Vet Magic Solution.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 22):
    old_img = f'../images/projects/project-7/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Free Vet Magic Solution - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-7.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
