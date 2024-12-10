"""
--- Day 6: Guard Gallivant ---
The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.
Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?

Your puzzle answer was 5531.

--- Part Two ---
While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and record the nightly status of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.

Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get stuck in a loop, making the rest of the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would like to know all of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

In the above example, there are only 6 different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use O to mark the new obstruction, | to show a position where the guard moves up/down, - to show a position where the guard moves left/right, and + to show a position where the guard moves both up/down and left/right.

Option one, put a printing press next to the guard's starting position:

....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...
Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:


....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...
Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...
Option four, put an alchemical retroencabulator near the bottom left corner:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...
Option five, put the alchemical retroencabulator a bit to the right instead:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...
Option six, put a tank of sovereign glue right next to the tank of universal solvent:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..
It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing. The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example, there are 6 different positions you could choose.

You need to get the guard stuck in a loop by adding a single new obstruction. How many different positions could you choose for this obstruction?

Your puzzle answer was 2165.
"""
input_map = []

with open("day_6.txt") as f:
    lines = f.readlines()
    
for line in lines:
    input_map.append(line.replace("\n", ""))

# Direction vectors for guard movement.
DIRECTIONS = {
    "^": (-1, 0),  # up
    ">": (0, 1),   # right
    "v": (1, 0),   # down
    "<": (0, -1)   # left
}
DIRECTION_ORDER = ["^", ">", "v", "<"]  # to determine turning right.

# Parse the map to find the guard's initial position and facing direction.
def parse_map(map_data):
    guard_position = None
    guard_facing = None
    obstacles = set()
    
    for row_idx, row in enumerate(map_data):
        for col_idx, cell in enumerate(row):
            if cell == "#":
                obstacles.add((row_idx, col_idx))
            elif cell in "^>v<":
                guard_position = (row_idx, col_idx)
                guard_facing = cell
    return guard_position, guard_facing, obstacles

# Simulate the guard's movement.
def simulate_guard(guard_position, guard_facing, obstacles, map_rows, map_cols):
    visited = set()
    current_position = guard_position
    current_facing = guard_facing

    while True:
        visited.add(current_position)
        next_row, next_col = (
            current_position[0] + DIRECTIONS[current_facing][0],
            current_position[1] + DIRECTIONS[current_facing][1],
        )
        
        # Check if next position is outside the map boundaries.
        if not (0 <= next_row < map_rows and 0 <= next_col < map_cols):
            break

        # Check if the next position is an obstacle.
        if (next_row, next_col) in obstacles:
            # Turn right (update direction).
            current_facing = DIRECTION_ORDER[
                (DIRECTION_ORDER.index(current_facing) + 1) % 4
            ]
        else:
            # Move forward.
            current_position = (next_row, next_col)
    
    return visited

# Main logic to compute distinct positions visited.
guard_position, guard_facing, obstacles = parse_map(input_map)
map_rows = len(input_map)
map_cols = len(input_map[0])
visited_positions = simulate_guard(guard_position, guard_facing, obstacles, map_rows, map_cols)

# Output the count of distinct positions visited.
print(len(visited_positions))



def simulate_with_obstruction(guard_position, guard_facing, obstacles, map_rows, map_cols, test_obstruction):
    """
    Simulate the guard's movement with a potential obstruction added.
    Returns True if the guard gets stuck in a loop, False otherwise.
    """
    visited_states = set()  # Track (position, facing direction) states
    current_position = guard_position
    current_facing = guard_facing

    # Add the test obstruction
    if test_obstruction:
        obstacles.add(test_obstruction)

    while True:
        state = (current_position, current_facing)
        if state in visited_states:
            # Loop detected
            if test_obstruction:
                obstacles.remove(test_obstruction)  # Clean up
            return True
        visited_states.add(state)

        next_row, next_col = (
            current_position[0] + DIRECTIONS[current_facing][0],
            current_position[1] + DIRECTIONS[current_facing][1],
        )

        # Check if next position is outside the map boundaries.
        if not (0 <= next_row < map_rows and 0 <= next_col < map_cols):
            break

        # Check if the next position is an obstacle.
        if (next_row, next_col) in obstacles:
            # Turn right (update direction).
            current_facing = DIRECTION_ORDER[
                (DIRECTION_ORDER.index(current_facing) + 1) % 4
            ]
        else:
            # Move forward.
            current_position = (next_row, next_col)

    # No loop detected; clean up and return
    if test_obstruction:
        obstacles.remove(test_obstruction)
    return False


def find_valid_obstruction_positions(input_map):
    """
    Find all positions where adding an obstruction would trap the guard in a loop.
    """
    guard_position, guard_facing, obstacles = parse_map(input_map)
    map_rows = len(input_map)
    map_cols = len(input_map[0])
    valid_positions = set()

    # Test all empty spaces (excluding guard's starting position)
    for row in range(map_rows):
        for col in range(map_cols):
            position = (row, col)
            if position not in obstacles and position != guard_position:
                if simulate_with_obstruction(guard_position, guard_facing, obstacles, map_rows, map_cols, position):
                    valid_positions.add(position)

    return valid_positions


# Find all valid positions for the obstruction in the input map.
valid_obstruction_positions = find_valid_obstruction_positions(input_map)

# Output the number of valid positions.
print(len(valid_obstruction_positions))
