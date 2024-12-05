def find_floor(instructions):
    floor = 0
    for char in instructions:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    return floor

def first_enter_basement(instructions):
    floor = 0
    for position, char in enumerate(instructions, start=1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            return position
    return None

with open('day_1.txt') as f:
    instructions = f.read()

print(find_floor(instructions))

print(first_enter_basement(instructions))