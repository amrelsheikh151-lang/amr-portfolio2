# Remove f_auto,q_auto from all Cloudinary URLs for original quality
with open(r'd:\website amr\amr portfolio\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the optimization parameters
content = content.replace('/f_auto,q_auto/', '/')
content = content.replace('f_auto,q_auto/', '')

with open(r'd:\website amr\amr portfolio\index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("Removed f_auto,q_auto from all URLs - images now use original quality!")
