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

def search(vec, input_map, target_str, row, col):
    if not target_str:  # base case: found the string
        return True

    if row < 0 or row >= len(input_map) or col < 0 or col >= len(input_map[row]):
        return False

    current_char = input_map[row][col]
    next_char = target_str[0]

    if current_char == next_char:
        dir_x, dir_y = vec
        return search(vec, input_map, target_str[1:], row + dir_y, col + dir_x)
    else:
        return False

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

with open("day_4.txt", "r") as f:
    input_lines = f.read().strip().splitlines()

input_map = {row: line for row, line in enumerate(input_lines)}

part1_result = part1(input_map)

print(f"Result Part 1 = {part1_result}")
