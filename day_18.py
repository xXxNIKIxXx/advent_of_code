"""
--- Day 18: Like a GIF For Your Yard ---
After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.
The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

Your puzzle answer was 814.

--- Part Two ---
You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#
After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?

Your puzzle answer was 924.
"""
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