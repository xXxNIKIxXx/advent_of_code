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