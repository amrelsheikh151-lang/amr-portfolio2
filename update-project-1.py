# Update project-1.html with Sea Air Logistics images
cloudinary_images = [
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472900/imgi_300_46d477216147463.677ba071988e0_qnjno5.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472906/imgi_307_8a0b50216147463.677ba07199268_s8f7tk.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472908/imgi_305_9f55bf216147463.677ba07199b8a_ac3d8t.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472925/imgi_303_ecdb8e216147463.677ba07199710_cz9ndg.jpg",
    "https://res.cloudinary.com/dwib2lgzp/image/upload/v1765472920/imgi_310_a43591216147463.677ba07198df7_cqgols.jpg"
]

with open(r'd:\website amr\amr portfolio\projects\project-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update title and description
content = content.replace('ALOMDa Home Design', 'Sea Air Logistics Company')
content = content.replace('Brand Identity', 'Brand Design')
content = content.replace('Complete brand identity design for ALOMDa Home Design based in UAE.', 'Complete brand design for Sea Air Logistics Company.')
content = content.replace('21 Images', '5 Images')

# Replace gallery images
for i in range(1, 22):  # Remove old images
    old_img = f'../images/projects/project-1/img{i}.jpg'
    if i <= 5:
        # Replace with Cloudinary image
        new_img = cloudinary_images[i-1]
        content = content.replace(old_img, new_img)
    else:
        # Remove extra gallery items
        content = content.replace(f'''            <div class="gallery-item">
                <img src="{old_img}" alt="ALOMDa Home Design - Image {i}" loading="lazy">
            </div>''', '')

with open(r'd:\website amr\amr portfolio\projects\project-1.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("Updated project-1.html with 5 Cloudinary images!")
