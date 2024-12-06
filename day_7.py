"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

Your puzzle answer was 16076.

--- Part Two ---
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

Your puzzle answer was 2797.
"""
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