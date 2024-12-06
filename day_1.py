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