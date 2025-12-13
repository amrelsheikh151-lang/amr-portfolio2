# Add Project 18: Viral
import re

project_num = 18
project_name = "Viral"
category = "campaign"
category_name = "Marketing Campaign"
description = "Complete project for Viral."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472941/imgi_300_42f02f224231697.6807a35227193_mr1el3.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472965/imgi_300_bf3b25224301985.6808c07c291e1_g6gn4y.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472922/imgi_300_8d6678224301895.6808c02e1da87_kke5ro.jpg"
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

# Update project-18.html
with open(r'd:\website amr\amr portfolio\projects\project-18.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('Tanbool  Come Back Capmaign', project_name)
project_content = project_content.replace('Marketing Design', category_name)
project_content = project_content.replace('Complete marketing design for Tanbool  Come Back Capmaign.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 22):
    old_img = f'../images/projects/project-18/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Tanbool  Come Back Capmaign - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-18.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
