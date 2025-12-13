# Check all projects to verify image counts
import os
import re

projects_data = {
    1: ("Sea Air Logistics", 5),
    2: ("ALOMDa Home Design", 7),
    3: ("Bulgarian Company", 8),
    4: ("Bulgarian vemo products", 4),
    5: ("Elhamamy Difference Campaign", 8),
    6: ("Elmazraa Company Natural Health Campaign", 6),
    7: ("Elrawda Campaign", 4),
    8: ("Free Vet Magic Solution Campaign", 5),
    9: ("Free Vet Nutrition Campaign", 4),
    10: ("German Gladiator Poultry", 3),
    11: ("German Copmany Product", 3),
    12: ("Italian Company Campaign", 4),
    13: ("Nour AL-Islam", 6),
    14: ("Ramdan Series", 7),
    15: ("Rawda 2", 4),
    16: ("Royal Poultry Campaign", 4),
    17: ("Tanbool Come Back Campaign", 4),
    18: ("Viral", 3),
    19: ("Viral2", 3),
    20: ("Printing", 25)
}

print("Checking all project files...")
print("=" * 60)

issues = []

for project_num, (project_name, expected_count) in projects_data.items():
    file_path = rf'd:\website amr\amr portfolio\projects\project-{project_num}.html'
    
    if not os.path.exists(file_path):
        issues.append(f"Project {project_num}: FILE NOT FOUND")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count gallery items
    gallery_items = content.count('<div class="gallery-item">')
    
    # Check if project name is correct
    name_found = project_name in content or project_name.replace(' ', '') in content.replace(' ', '')
    
    status = "OK" if gallery_items == expected_count else "WRONG"
    
    print(f"Project {project_num:2d}: {project_name:40s} | Expected: {expected_count:2d} | Found: {gallery_items:2d} | {status}")
    
    if gallery_items != expected_count:
        issues.append(f"Project {project_num}: Expected {expected_count} images, found {gallery_items}")

print("=" * 60)

if issues:
    print(f"\nFOUND {len(issues)} ISSUES:")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("\nALL PROJECTS ARE CORRECT!")
