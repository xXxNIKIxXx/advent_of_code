from collections import deque

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

def solve_molecule_problem(file_path):
    # Read the input
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    
    # Parse the replacements and the target molecule
    replacements = []
    for line in lines:
        if '=>' in line:
            src, target = line.split(' => ')
            replacements.append((target, src))  # Reverse the replacements for backward application
        elif line.strip():  # The target molecule is the last non-empty line
            target_molecule = line.strip()
    
    # Sort replacements by decreasing target length for greedy application
    replacements.sort(key=lambda x: len(x[0]), reverse=True)
    
    # Greedy reduction to go from target molecule to 'e'
    current_molecule = target_molecule
    steps = 0
    while current_molecule != 'e':
        for target, src in replacements:
            if target in current_molecule:
                # Apply the replacement
                current_molecule = current_molecule.replace(target, src, 1)
                steps += 1
                break
    
    return steps

# Solve the problem using the provided input file
file_path = 'day_19.txt'
result = solve_molecule_problem(file_path)
print(f"Fewest number of steps to produce the medicine: {result}")
