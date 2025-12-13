# Remove all project cards from index.html
with open(r'd:\website amr\amr portfolio\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find work-grid section and remove all projects
new_lines = []
in_work_grid = False
skip_until_closing = 0

for i, line in enumerate(lines):
    if '<div class="work-grid">' in line:
        in_work_grid = True
        new_lines.append(line)
        new_lines.append('                <!-- Projects will be added here -->\n')
        continue
    
    if in_work_grid and '</div>' in line and 'work-grid' not in line:
        skip_until_closing += 1
        continue
    
    if in_work_grid and '</section>' in line:
        # Add closing div for work-grid
        new_lines.append('            </div>\n')
        new_lines.append(line)
        in_work_grid = False
        continue
    
    if not in_work_grid:
        new_lines.append(line)

with open(r'd:\website amr\amr portfolio\index.html', 'w', encoding='utf-8', newline='') as f:
    f.writelines(new_lines)

print("Removed all project cards!")
