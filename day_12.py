import json

def sum_numbers(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(sum_numbers(item) for item in data)
    elif isinstance(data, dict):
        return sum(sum_numbers(value) for value in data.values())
    return 0

with open('day_12.txt', 'r') as file:
    data = json.load(file)

total_sum = sum_numbers(data)
print(f"The sum of all numbers in the document is: {total_sum}")
