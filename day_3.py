import re

def extract_and_multiply(input_string):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    
    matches = re.findall(pattern, input_string)
    
    total_sum = 0
    
    for match in matches:
        numbers = re.findall(r'\d{1,3}', match)
        if len(numbers) == 2:
            x, y = map(int, numbers)
            total_sum += x * y
    
    return total_sum


def extract_and_multiply_with_conditions(input_string):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    
    matches = re.findall(pattern, input_string)
    
    total_sum = 0
    enabled = True
    
    for match in re.finditer(r'do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)', input_string):
        instruction = match.group()
        
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled and instruction.startswith("mul"):
            numbers = re.findall(r'\d{1,3}', instruction)
            if len(numbers) == 2:
                x, y = map(int, numbers)
                total_sum += x * y
    
    return total_sum

corrupted_memory = ""

with open("day_3.txt") as file:
    lines = file.readlines()

for line in lines:
    corrupted_memory = corrupted_memory + line

result = extract_and_multiply(corrupted_memory)
print(result)

result_with_conditions = extract_and_multiply_with_conditions(corrupted_memory)
print(result_with_conditions)