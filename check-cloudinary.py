import requests
import base64
import json

# Cloudinary credentials
cloud_name = "dwib2lgzp"
api_key = "868152855977815"
api_secret = "gRymDRDGDjPQ07iYrEkJdMRoodQ"

# Create basic auth
auth_str = f"{api_key}:{api_secret}"
auth_bytes = auth_str.encode('ascii')
auth_b64 = base64.b64encode(auth_bytes).decode('ascii')

headers = {"Authorization": f"Basic {auth_b64}"}

# Get folders
print("Fetching folders...")
url = f"https://api.cloudinary.com/v1_1/{cloud_name}/folders"
response = requests.get(url, headers=headers)
folders_data = response.json()

print(f"\nFolders found: {len(folders_data.get('folders', []))}")
for folder in folders_data.get('folders', []):
    print(f"  - {folder['name']}")

# Get all resources
print("\nFetching all images...")
url = f"https://api.cloudinary.com/v1_1/{cloud_name}/resources/image?max_results=500"
response = requests.get(url, headers=headers)
resources_data = response.json()

print(f"Total images: {len(resources_data.get('resources', []))}")

# Group by folder
folder_images = {}
for resource in resources_data.get('resources', []):
    public_id = resource['public_id']
    
    # Skip samples
    if public_id.startswith('samples/'):
        continue
    
    if '/' in public_id:
        folder = public_id.rsplit('/', 1)[0]
        if folder not in folder_images:
            folder_images[folder] = []
        folder_images[folder].append(public_id)

print(f"\nProject folders with images: {len(folder_images)}")
for folder, images in sorted(folder_images.items()):
    print(f"\n{folder}: {len(images)} images")
    for img in sorted(images)[:2]:  # Show first 2
        print(f"  - {img}")

# Save
with open('cloudinary-project-images.json', 'w', encoding='utf-8') as f:
    json.dump(folder_images, f, indent=2, ensure_ascii=False)

print("\nSaved to cloudinary-project-images.json")
