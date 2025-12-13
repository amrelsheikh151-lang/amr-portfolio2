"""
Convert all project images to lazy loading except the first 3
This will make the page load MUCH faster by only loading visible images
"""

import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all project images
pattern = r'(<img src="https://res\.cloudinary\.com/[^"]+"\s+alt="[^"]+"\s+class="project-bg-img"\s+loading=")([^"]+)(")'

count = 0
def replace_loading(match):
    global count
    count += 1
    prefix = match.group(1)
    current_loading = match.group(2)
    suffix = match.group(3)
    
    # Keep first 3 as "eager", rest as "lazy"
    if count <= 3:
        return f'{prefix}eager{suffix}'
    else:
        return f'{prefix}lazy{suffix}'

# Replace all loading attributes
html_updated = re.sub(pattern, replace_loading, html)

print(f"Updated {count} images:")
print(f"  - First 3: loading='eager' (load immediately)")
print(f"  - Remaining {count-3}: loading='lazy' (load when visible)")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_updated)

print("\nindex.html updated!")
print("Page will now load MUCH faster - only visible images load first!")
