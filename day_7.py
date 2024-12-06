import re

# Read the input file
with open('day_7.txt') as f:
    instructions = f.read().strip().split('\n')

# Dictionary to store the values of the wires
wires = {}

# Regular expressions to match different types of instructions
value_re = re.compile(r'(\d+) -> (\w+)')
wire_re = re.compile(r'(\w+) -> (\w+)')
and_re = re.compile(r'(\w+) AND (\w+) -> (\w+)')
or_re = re.compile(r'(\w+) OR (\w+) -> (\w+)')
lshift_re = re.compile(r'(\w+) LSHIFT (\d+) -> (\w+)')
rshift_re = re.compile(r'(\w+) RSHIFT (\d+) -> (\w+)')
not_re = re.compile(r'NOT (\w+) -> (\w+)')

# Function to get the value of a wire
def get_value(wire):
    if wire.isdigit():
        return int(wire)
    if wire not in wires:
        wires[wire] = evaluate(wire)
    return wires[wire]

# Function to evaluate the value of a wire
def evaluate(wire):
    for instruction in instructions:
        if value_re.match(instruction):
            value, target = value_re.match(instruction).groups()
            if target == wire:
                return int(value)
        elif wire_re.match(instruction):
            source, target = wire_re.match(instruction).groups()
            if target == wire:
                return get_value(source)
        elif and_re.match(instruction):
            x, y, target = and_re.match(instruction).groups()
            if target == wire:
                return get_value(x) & get_value(y)
        elif or_re.match(instruction):
            x, y, target = or_re.match(instruction).groups()
            if target == wire:
                return get_value(x) | get_value(y)
        elif lshift_re.match(instruction):
            x, shift, target = lshift_re.match(instruction).groups()
            if target == wire:
                return get_value(x) << int(shift)
        elif rshift_re.match(instruction):
            x, shift, target = rshift_re.match(instruction).groups()
            if target == wire:
                return get_value(x) >> int(shift)
        elif not_re.match(instruction):
            source, target = not_re.match(instruction).groups()
            if target == wire:
                return ~get_value(source) & 0xFFFF

# Get the value of wire 'a'
result = get_value('a')
print(f"The signal ultimately provided to wire 'a' is: {result}")

# Override wire 'b' with the value of wire 'a'
wires = {'b': result}

# Reset the other wires
instructions = [instr for instr in instructions if not instr.endswith(' -> b')]

# Get the new value of wire 'a'
new_result = get_value('a')
print(f"The new signal ultimately provided to wire 'a' is: {new_result}")