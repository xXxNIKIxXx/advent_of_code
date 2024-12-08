def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    replacements = []
    molecule = lines[-1].strip()
    
    for line in lines[:-2]:
        parts = line.strip().split(" => ")
        replacements.append((parts[0], parts[1]))
    
    return replacements, molecule

def generate_new_molecules(replacements, molecule):
    new_molecules = set()
    
    for old, new in replacements:
        start = 0
        while True:
            start = molecule.find(old, start)
            if start == -1:
                break
            new_molecule = molecule[:start] + new + molecule[start + len(old):]
            new_molecules.add(new_molecule)
            start += 1
    
    return new_molecules

replacements, molecule = read_input('day_19.txt')
new_molecules = generate_new_molecules(replacements, molecule)
print(f"Number of distinct molecules: {len(new_molecules)}")
