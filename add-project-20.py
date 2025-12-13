# Add Project 20: Printing
import re

project_num = 20
project_name = "Printing"
category = "print"
category_name = "Print Design"
description = "Complete project for Printing."
images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472649/1_2_rzv1zs.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472657/1_3_bctxya.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472686/1_1_lyplzw.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472662/imgi_335_05b37e206678287.66d05c5c3c98c_rqjf2s.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472669/imgi_336_8e7b7a206678287.66d05c5c3da44_wysrxe.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472675/imgi_343_699eca206678287.66d05c5c3ec41_1_y1yeki.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472683/imgi_345_df5897206678287.66d05c5c3d011_scqgqi.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472689/imgi_350_58e873206678287.66d05c5c3c3fa_szba1d.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472694/imgi_353_6ba2b5206678287.66d05c5c4051a_ldiqrf.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472699/imgi_358_3461a7206678287.66d05c5c3bdd8_b1wrik.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472702/imgi_338_feb936206678287.66d05c5c3e482_x0ljti.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472705/imgi_363_895232206678287.66d05c5c45f08_vdctjm.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472708/imgi_367_859966206678287.66d05c5c44900_d3tru1.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472711/imgi_334_c1edb2206678287.66d05c5c4692a_bsm204.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472714/imgi_379_8dce0a206678287.66d05c5c49e64_iq7bcz.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472717/imgi_382_26fc77206678287.66d05c5c4a791_chae5r.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472721/imgi_375_c9c15c206678287.66d05c5c49340_u6duha.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472723/imgi_385_c28734206678287.66d05c5c44088_n165vw.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472723/imgi_373_ed0364206678287.66d05c5c48844_qtlqqe.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472716/imgi_362_45ab5a206678287.66d05c5c42313_gzoe4u.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472728/imgi_364_440ec0206678287.66d05c5c43abf_i4heg2.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472731/imgi_352_ed4a58206678287.66d05c5c42c6e_tt6jzn.png",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472731/%D9%85%D9%88%D9%83%D8%A8_%D9%85%D9%8A%D8%AC%D8%A7_3_xkbnn5.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472770/%D9%85%D9%88%D9%83%D8%A8_%D9%85%D9%8A%D8%AC%D8%A7_4_g8grki.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472755/imgi_400_e896c3206678287.66d05c5c3b58c_h5lpkb.png"
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

# Update project-20.html
with open(r'd:\website amr\amr portfolio\projects\project-20.html', 'r', encoding='utf-8') as f:
    project_content = f.read()

project_content = project_content.replace('Viral2', project_name)
project_content = project_content.replace('Marketing Design', category_name)
project_content = project_content.replace('Complete marketing design for Viral2.', description)
project_content = re.sub(r'\d+ Images', f'{len(images)} Images', project_content)

for i in range(1, 30):
    old_img = f'../images/projects/project-20/img{i}.jpg'
    if i <= len(images):
        new_img = images[i-1]
        project_content = project_content.replace(old_img, new_img)
        project_content = project_content.replace(f'Viral2 - Image {i}', f'{project_name} - Image {i}')
    else:
        pattern = f'''            <div class="gallery-item">
                <img src="{re.escape(old_img)}" alt="[^"]*" loading="lazy">
            </div>'''
        project_content = re.sub(pattern, '', project_content)

with open(r'd:\website amr\amr portfolio\projects\project-20.html', 'w', encoding='utf-8', newline='') as f:
    f.write(project_content)

print(f"Project {project_num} added: {project_name} ({len(images)} images)")
print("Portfolio complete! All 20 projects added with Cloudinary images!")
