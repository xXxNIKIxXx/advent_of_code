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