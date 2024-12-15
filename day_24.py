import itertools
import math

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]

def find_best_group(weights, group_count):
    total_weight = sum(weights)
    target_weight = total_weight // group_count

    for group_size in range(1, len(weights)):
        valid_groups = [group for group in itertools.combinations(weights, group_size) if sum(group) == target_weight]
        if valid_groups:
            min_qe_group = min(valid_groups, key=lambda group: math.prod(group))
            return min_qe_group, math.prod(min_qe_group)

    return None, None

weights = read_input('day_24.txt')
group_count = 3
best_group, quantum_entanglement = find_best_group(weights, group_count)

if best_group:
    print(f"The best group is: {best_group}")
    print(f"The quantum entanglement is: {quantum_entanglement}")
else:
    print("No valid group found")
    
group_count = 4
best_group, quantum_entanglement = find_best_group(weights, group_count)

if best_group:
    print(f"The best group is: {best_group}")
    print(f"The quantum entanglement is: {quantum_entanglement}")
else:
    print("No valid group found")
