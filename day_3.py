import re

def extract_and_multiply(input_string):
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    
    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    
    total_sum = 0
    
    for match in matches:
        # Extract the numbers from the match
        numbers = re.findall(r'\d{1,3}', match)
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