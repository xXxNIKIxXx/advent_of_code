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


def count_houses_with_presents_with_robo_santa(directions):
    # Starting positions for Santa and Robo-Santa
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    # Set to keep track of visited houses
    visited_houses = set()
    # Add the starting house
    visited_houses.add((santa_x, santa_y))

    # Process each direction
    for i, direction in enumerate(directions):
        if i % 2 == 0:  # Santa's turn
            if direction == '^':
                santa_y += 1
            elif direction == 'v':
                santa_y -= 1
            elif direction == '>':
                santa_x += 1
            elif direction == '<':
                santa_x -= 1
            visited_houses.add((santa_x, santa_y))
        else:  # Robo-Santa's turn
            if direction == '^':
                robo_y += 1
            elif direction == 'v':
                robo_y -= 1
            elif direction == '>':
                robo_x += 1
            elif direction == '<':
                robo_x -= 1
            visited_houses.add((robo_x, robo_y))

    # Return the number of unique houses visited
    return len(visited_houses)

with open('2015/day_3.txt', 'r') as file:
    directions = file.read().strip()

print(count_houses_with_presents(directions))

print(count_houses_with_presents_with_robo_santa(directions))