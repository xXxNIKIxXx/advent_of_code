"""
--- Day 19: Medicine for Rudolph ---
Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:

H => HO
H => OH
O => HH
Given the replacements above and starting with HOH, the following molecules could be generated:

HOOH (via H => HO on the first H).
HOHO (via H => HO on the second H).
OHOH (via H => OH on the first H).
HOOH (via H => OH on the second H).
HHHH (via O => HH).
So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and three from O).

The machine replaces without regard for the surrounding characters. For example, given the string H2O, the transition H => OO would result in OO2O.

Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine. How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?

Your puzzle answer was 535.

--- Part Two ---
Now that the machine is calibrated, you're ready to begin molecule fabrication.

Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time, just like the ones during calibration.

For example, suppose you have the following replacements:

e => H
e => O
H => HO
H => OH
O => HH
If you'd like to make HOH, you start with e, and then make the following replacements:

e => O to get O
O => HH to get HH
H => OH (on the second H) to get HOH
So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps.

How long will it take to make the medicine? Given the available replacements and the medicine molecule in your puzzle input, what is the fewest number of steps to go from e to the medicine molecule?

Your puzzle answer was 212.
"""
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
