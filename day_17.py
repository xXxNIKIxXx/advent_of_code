from itertools import combinations

def count_combinations(containers, target):
    count = 0
    for i in range(1, len(containers) + 1):
        for combo in combinations(containers, i):
            if sum(combo) == target:
                count += 1
    return count


with open('day_17.txt') as f:
    containers = [int(line.strip()) for line in f.readlines()]

target = 150
result = count_combinations(containers, target)
print(f'Total combinations: {result}')

def min_container_combinations(containers, target):
    min_count = float('inf')
    min_combinations = 0
    for i in range(1, len(containers) + 1):
        for combo in combinations(containers, i):
            if sum(combo) == target:
                if i < min_count:
                    min_count = i
                    min_combinations = 1
                elif i == min_count:
                    min_combinations += 1
    return min_combinations

min_combinations = min_container_combinations(containers, target)
print(f'Minimum container combinations: {min_combinations}')