# Add Project 5: Elhamamy Difference Campaign
import re

project_num = 5
project_name = "Elhamamy Difference Campaign"
category = "campaign"
category_name = "Marketing Campaign"
description = "Complete project for Elhamamy Difference Campaign."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472274/imgi_309_b14488206671493.66d049ae8bac0_g5ksst.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472262/imgi_321_85903c206671493.66d049ae8a1db_qbd4ax.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472237/imgi_317_81b838206671493.66d049ae8c164_wetj7m.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472283/imgi_311_e5b4d5206671493.66d049ae88c02_ndth0r.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472246/imgi_319_81cfbf206671493.66d049ae8aa64_vhbir1.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472262/imgi_318_40b4a4206671493.66d049ae8b2fa_mc9ufd.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472256/imgi_313_0ec2e5206671493.66d049ae89a64_zo5xaj.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472272/imgi_315_9a7efa206671493.66d049ae89360_l4soj4.png"
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

# Update project-5.html
with open(r'd:\website amr\amr portfolio\projects\project-5.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('Elmazraa Natural Health', project_name)
project_content = project_content.replace('Health Campaign', category_name)
project_content = project_content.replace('Complete health campaign for Elmazraa Natural Health.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 22):
    old_img = f'../images/projects/project-5/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Elmazraa Natural Health - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-5.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
