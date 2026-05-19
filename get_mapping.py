import json

with open('medical_insurance.ipynb', 'r') as f:
    notebook = json.load(f)

for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        if 'replace' in source or 'map' in source or 'encoder' in source.lower():
            print(source)
            print("---")
