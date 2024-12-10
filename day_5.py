from collections import defaultdict, deque

def parse_input(file_path):
    """Parse the input file to extract ordering rules and updates."""
    with open(file_path, 'r') as file:
        sections = file.read().split("\n\n")
        rules_section = sections[0].splitlines()
        updates_section = sections[1].splitlines()

    rules = []
    for rule in rules_section:
        x, y = map(int, rule.split('|'))
        rules.append((x, y))

    updates = []
    for update in updates_section:
        updates.append(list(map(int, update.split(','))))

    return rules, updates

def is_update_valid(update, rules):
    """Check if an update adheres to the ordering rules."""
    index_map = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                return False
    return True


def middle_value(update):
    """Return the middle value of a list."""
    n = len(update)
    return update[n // 2]

def solve(file_path):
    """Solve both parts of the problem."""
    rules, updates = parse_input(file_path)

    # Part 1: Valid updates
    valid_updates = [update for update in updates if is_update_valid(update, rules)]
    valid_middle_sum = sum(middle_value(update) for update in valid_updates)


    return valid_middle_sum

# Example usage
file_path = "day_5.txt"  # Replace with your input file path
part1_result = solve(file_path)
print("Part 1: Sum of middle values of valid updates:", part1_result)
