import os

folders = ['input_pdfs', 'output_docs', 'scripts', 'database', 'screenshots']
base_path = '.' 

for folder in folders:
    path = os.path.join(base_path, folder)
    os.makedirs(path, exist_ok=True)

print("Folders created successfully!")
