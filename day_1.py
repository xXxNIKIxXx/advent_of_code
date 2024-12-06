"""
--- Day 1: No Time for a Taxicab ---
Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?

Your puzzle answer was 252.

--- Part Two ---
Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

Your puzzle answer was 143.
"""
# Read the input from the file
with open('day_1.txt', 'r') as file:
    directions = file.read().strip().split(', ')

# Initial position and direction
x, y = 0, 0
direction = 0  # 0: North, 1: East, 2: South, 3: West

# Define movement vectors for each direction
movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Process each direction
for move in directions:
    turn = move[0]
    steps = int(move[1:])
    
    # Update direction
    if turn == 'R':
        direction = (direction + 1) % 4
    elif turn == 'L':
        direction = (direction - 1) % 4
    
    # Move in the current direction
    x += movement[direction][0] * steps
    y += movement[direction][1] * steps

# Calculate the Manhattan distance
distance = abs(x) + abs(y)
print(f"The shortest path to the destination is {distance} blocks.")

# Track visited locations
visited = set()
visited.add((0, 0))

# Reset initial position and direction
x, y = 0, 0
direction = 0

# Find the first location visited twice
first_revisited_distance = None

for move in directions:
    turn = move[0]
    steps = int(move[1:])
    
    # Update direction
    if turn == 'R':
        direction = (direction + 1) % 4
    elif turn == 'L':
        direction = (direction - 1) % 4
    
    # Move step by step in the current direction
    for _ in range(steps):
        x += movement[direction][0]
        y += movement[direction][1]
        
        if (x, y) in visited and first_revisited_distance is None:
            first_revisited_distance = abs(x) + abs(y)
        visited.add((x, y))

print(f"The first location visited twice is {first_revisited_distance} blocks away.")