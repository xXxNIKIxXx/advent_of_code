def execute_instructions(instructions):
    registers = {'a': 0, 'b': 0}
    pc = 0  # program counter

    while pc < len(instructions):
        parts = instructions[pc].split()
        instr = parts[0]

        if instr == 'hlf':
            registers[parts[1]] //= 2
            pc += 1
        elif instr == 'tpl':
            registers[parts[1]] *= 3
            pc += 1
        elif instr == 'inc':
            registers[parts[1]] += 1
            pc += 1
        elif instr == 'jmp':
            pc += int(parts[1])
        elif instr == 'jie':
            if registers[parts[1][0]] % 2 == 0:
                pc += int(parts[2])
            else:
                pc += 1
        elif instr == 'jio':
            if registers[parts[1][0]] == 1:
                pc += int(parts[2])
            else:
                pc += 1

    return registers['b']

if __name__ == "__main__":
    with open('day_23.txt') as f:
        instructions = [line.strip() for line in f.readlines()]
    result = execute_instructions(instructions)
    print(f"The value in register b is {result}")