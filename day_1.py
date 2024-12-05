def find_floor(instructions):
    floor = 0
    for char in instructions:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    return floor

with open('day_1.txt') as f:
    instructions = f.read()

print(find_floor(instructions))