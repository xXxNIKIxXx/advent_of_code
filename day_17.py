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
