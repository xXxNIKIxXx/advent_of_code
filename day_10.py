"""
--- Day 10: Elves Look, Elves Say ---
Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

For example:

1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).
Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

Your puzzle answer was 360154.

--- Part Two ---
Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of Life fame).

Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?

Your puzzle answer was 5103798.
"""
def look_and_say(sequence):
    result = []
    i = 0
    while i < len(sequence):
        count = 1
        while i + 1 < len(sequence) and sequence[i] == sequence[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + sequence[i])
        i += 1
    return ''.join(result)

def apply_look_and_say(sequence, iterations):
    for _ in range(iterations):
        sequence = look_and_say(sequence)
    return sequence

puzzle_input = "1113122113"
result = apply_look_and_say(puzzle_input, 40)
print(f"Length of the result after 40 iterations: {len(result)}")

result_part_two = apply_look_and_say(puzzle_input, 50)
print(f"Length of the result after 50 iterations: {len(result_part_two)}")