
"""
--- Day 4: Ceres Search ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?

Your puzzle answer was 2500.

--- Part Two ---
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?

Your puzzle answer was 1933.
"""
# Define the direction vectors for part 1 and part 2
part1_dirs = [
    (1, 0),  # right
    (-1, 0),  # left
    (0, 1),  # down
    (0, -1),  # up
    (1, 1),  # down-right
    (-1, 1),  # down-left
    (1, -1),  # up-right
    (-1, -1)  # up-left
]

part2_dirs = [
    (1, 1),  # down-right
    (-1, 1),  # down-left
    (1, -1),  # up-right
    (-1, -1)  # up-left
]

# Helper function to search for the string starting from a position
def search(vec, input_map, target_str, row, col):
    if not target_str:  # base case: found the string
        return True

    if row < 0 or row >= len(input_map) or col < 0 or col >= len(input_map[row]):
        return False

    current_char = input_map[row][col]
    next_char = target_str[0]

    if current_char == next_char:
        # Continue searching in the direction indicated by vec
        dir_x, dir_y = vec
        return search(vec, input_map, target_str[1:], row + dir_y, col + dir_x)
    else:
        return False

# Part 1: Count occurrences of the string "XMAS" in all directions
def part1(input_map):
    total_count = 0
    for row, line in input_map.items():
        line_results = []
        for i in range(len(line)):
            line_result = sum(
                search(vec, input_map, "XMAS", row, i) for vec in part1_dirs
            )
            line_results.append(line_result)
        total_count += sum(line_results)
    return total_count

# Part 2: Count positions where "MAS" can be found in any of the four directions
def part2(input_map):
    positions = []

    for row, line in input_map.items():
        for col in range(len(line)):
            for vec in part2_dirs:
                pos = (col + vec[0], row + vec[1])
                if search(vec, input_map, "MAS", row, col):
                    positions.append(pos)

    # Count positions that occur exactly twice and return the unique count
    unique_positions = set(positions)
    valid_positions = [
        pos for pos in unique_positions if positions.count(pos) == 2
    ]
    return len(valid_positions)

# Read input and prepare the input map
with open("day_4.txt", "r") as f:
    input_lines = f.read().strip().splitlines()

input_map = {row: line for row, line in enumerate(input_lines)}

# Run tasks for part 1 and part 2
part1_result = part1(input_map)
part2_result = part2(input_map)

# Output results
print(f"Result Part 1 = {part1_result}")
print(f"Result Part 2 = {part2_result}")
