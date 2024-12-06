"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
Your puzzle answer was 2572.

--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
Your puzzle answer was 2631.
"""
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