"""
Fix all Cloudinary image URLs in index.html to use mobile-optimized versions
This will make images load INSTANTLY on mobile without waiting for JavaScript
"""

import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all Cloudinary image URLs
pattern = r'(https://res\.cloudinary\.com/dwib2lgzp/image/upload/)(v\d+/)([^"]+)'

def optimize_url(match):
    base = match.group(1)
    version = match.group(2)
    image_id = match.group(3)
    
    # Add mobile optimization parameters
    # w_400 = max width 400px (perfect for mobile)
    # q_auto = automatic quality
    # f_auto = automatic format (WebP on supported browsers)
    # c_limit = don't upscale
    optimized = f"{base}w_400,q_auto,f_auto,c_limit/{version}{image_id}"
    
    return optimized

# Replace all URLs
html_optimized = re.sub(pattern, optimize_url, html)

# Count replacements
original_count = len(re.findall(pattern, html))
print(f"Optimized {original_count} image URLs")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_optimized)

print("index.html updated with optimized image URLs!")
print("Images will now load INSTANTLY on mobile!")
