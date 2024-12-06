import itertools

def parse_input(file_path):
    happiness = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            person1 = parts[0]
            person2 = parts[-1][:-1]
            value = int(parts[3]) * (1 if parts[2] == 'gain' else -1)
            if person1 not in happiness:
                happiness[person1] = {}
            happiness[person1][person2] = value
    return happiness

def calculate_happiness(arrangement, happiness):
    total_happiness = 0
    for i in range(len(arrangement)):
        person1 = arrangement[i]
        person2 = arrangement[(i + 1) % len(arrangement)]
        total_happiness += happiness[person1][person2]
        total_happiness += happiness[person2][person1]
    return total_happiness

def find_optimal_arrangement(happiness):
    people = list(happiness.keys())
    max_happiness = float('-inf')
    for arrangement in itertools.permutations(people):
        current_happiness = calculate_happiness(arrangement, happiness)
        if current_happiness > max_happiness:
            max_happiness = current_happiness
    return max_happiness

happiness = parse_input('day_13.txt')
optimal_happiness = find_optimal_arrangement(happiness)
print(f"The total change in happiness for the optimal seating arrangement is {optimal_happiness}")


# Add yourself to the happiness dictionary with 0 happiness change with everyone
for person in happiness.keys():
    happiness[person]['You'] = 0
happiness['You'] = {person: 0 for person in happiness.keys()}

# Find the optimal arrangement including yourself
optimal_happiness_with_you = find_optimal_arrangement(happiness)
print(f"The total change in happiness for the optimal seating arrangement including yourself is {optimal_happiness_with_you}")