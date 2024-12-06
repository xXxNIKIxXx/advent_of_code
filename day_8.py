import re

def count_code_characters(s):
    return len(s)

def count_memory_characters(s):
    # Remove the surrounding double quotes
    s = s[1:-1]
    # Replace escaped backslashes and quotes
    s = s.replace('\\\\', '\\')
    s = s.replace('\\"', '"')
    # Replace hexadecimal escape sequences
    s = re.sub(r'\\x[0-9a-fA-F]{2}', 'X', s)
    return len(s)

with open('day_8.txt', 'r') as file:
    lines = file.readlines()

total_code_characters = 0
total_memory_characters = 0

for line in lines:
    line = line.strip()
    total_code_characters += count_code_characters(line)
    total_memory_characters += count_memory_characters(line)

result = total_code_characters - total_memory_characters
print(f"Total characters of code: {total_code_characters}")
print(f"Total characters in memory: {total_memory_characters}")
print(f"Difference: {result}")

def encode_string(s):
    # Escape backslashes and double quotes
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    # Add surrounding double quotes
    s = f'"{s}"'
    return s

total_encoded_characters = 0

for line in lines:
    line = line.strip()
    encoded_line = encode_string(line)
    total_encoded_characters += len(encoded_line)

result_encoded = total_encoded_characters - total_code_characters
print(f"Total characters of encoded strings: {total_encoded_characters}")
print(f"Difference between encoded and original: {result_encoded}")