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