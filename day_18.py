def parse_input(input_str):
    return [list(line) for line in input_str.strip().split('\n')]

def count_on_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == '#':
                count += 1
    return count

def step(grid):
    new_grid = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            on_neighbors = count_on_neighbors(grid, x, y)
            if grid[x][y] == '#' and on_neighbors in (2, 3):
                new_grid[x][y] = '#'
            elif grid[x][y] == '.' and on_neighbors == 3:
                new_grid[x][y] = '#'
    return new_grid

def count_lights_on(grid):
    return sum(row.count('#') for row in grid)

def animate_lights(input_str, steps):
    grid = parse_input(input_str)
    for _ in range(steps):
        grid = step(grid)
    return count_lights_on(grid)



with open('day_18.txt') as f:
    input_str = f.read()
steps = 100
print(animate_lights(input_str, steps))

def set_corners_on(grid):
    grid[0][0] = '#'
    grid[0][len(grid[0]) - 1] = '#'
    grid[len(grid) - 1][0] = '#'
    grid[len(grid) - 1][len(grid[0]) - 1] = '#'

def animate_lights_with_stuck_corners(input_str, steps):
    grid = parse_input(input_str)
    set_corners_on(grid)
    for _ in range(steps):
        grid = step(grid)
        set_corners_on(grid)
    return count_lights_on(grid)

print(animate_lights_with_stuck_corners(input_str, steps))