# Define the direction vectors for part 1 and part 2
part1_dirs = [
    (1, 0),  # right
    (-1, 0),  # left
    (0, 1),  # down
    (0, -1),  # up
    (1, 1),  # down-right
    (-1, 1),  # down-left
    (1, -1),  # up-right
    (-1, -1)  # up-left
]

part2_dirs = [
    (1, 1),  # down-right
    (-1, 1),  # down-left
    (1, -1),  # up-right
    (-1, -1)  # up-left
]

# Helper function to search for the string starting from a position
def search(vec, input_map, target_str, row, col):
    if not target_str:  # base case: found the string
        return True

    if row < 0 or row >= len(input_map) or col < 0 or col >= len(input_map[row]):
        return False

    current_char = input_map[row][col]
    next_char = target_str[0]

    if current_char == next_char:
        # Continue searching in the direction indicated by vec
        dir_x, dir_y = vec
        return search(vec, input_map, target_str[1:], row + dir_y, col + dir_x)
    else:
        return False

# Part 1: Count occurrences of the string "XMAS" in all directions
def part1(input_map):
    total_count = 0
    for row, line in input_map.items():
        line_results = []
        for i in range(len(line)):
            line_result = sum(
                search(vec, input_map, "XMAS", row, i) for vec in part1_dirs
            )
            line_results.append(line_result)
        total_count += sum(line_results)
    return total_count

# Part 2: Count positions where "MAS" can be found in any of the four directions
def part2(input_map):
    positions = []

    for row, line in input_map.items():
        for col in range(len(line)):
            for vec in part2_dirs:
                pos = (col + vec[0], row + vec[1])
                if search(vec, input_map, "MAS", row, col):
                    positions.append(pos)

    # Count positions that occur exactly twice and return the unique count
    unique_positions = set(positions)
    valid_positions = [
        pos for pos in unique_positions if positions.count(pos) == 2
    ]
    return len(valid_positions)

# Read input and prepare the input map
with open("day_4.txt", "r") as f:
    input_lines = f.read().strip().splitlines()

input_map = {row: line for row, line in enumerate(input_lines)}

# Run tasks for part 1 and part 2
part1_result = part1(input_map)
part2_result = part2(input_map)

# Output results
print(f"Result Part 1 = {part1_result}")
print(f"Result Part 2 = {part2_result}")
