def parse_instruction(instruction):
    parts = instruction.split()
    if parts[0] == "toggle":
        action = "toggle"
        start = tuple(map(int, parts[1].split(',')))
        end = tuple(map(int, parts[3].split(',')))
    else:
        action = "turn on" if parts[1] == "on" else "turn off"
        start = tuple(map(int, parts[2].split(',')))
        end = tuple(map(int, parts[4].split(',')))
    return action, start, end

def apply_instruction(grid, instruction):
    action, start, end = instruction
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            if action == "turn on":
                grid[x][y] = 1
            elif action == "turn off":
                grid[x][y] = 0
            elif action == "toggle":
                grid[x][y] = 1 - grid[x][y]

def count_lights(grid):
    return sum(sum(row) for row in grid)

grid = [[0] * 1000 for _ in range(1000)]
with open('day_6.txt') as f:
    instructions = f.readlines()

for instruction in instructions:
    parsed_instruction = parse_instruction(instruction.strip())
    apply_instruction(grid, parsed_instruction)

print(f"Number of lights that are lit: {count_lights(grid)}")