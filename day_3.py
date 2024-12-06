def count_houses_with_presents(directions):
    # Starting position
    x, y = 0, 0
    # Set to keep track of visited houses
    visited_houses = set()
    # Add the starting house
    visited_houses.add((x, y))

    # Process each direction
    for direction in directions:
        if direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1
        elif direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        # Add the new house to the set
        visited_houses.add((x, y))

    # Return the number of unique houses visited
    return len(visited_houses)

with open('2015/day_3.txt', 'r') as file:
    directions = file.read().strip()

print(count_houses_with_presents(directions))

