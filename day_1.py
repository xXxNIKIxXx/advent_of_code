def read_frequency_changes(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def calculate_resulting_frequency(changes):
    frequency = 0
    for change in changes:
        frequency += change
    return frequency

changes = read_frequency_changes('day_1.txt')
resulting_frequency = calculate_resulting_frequency(changes)
print(f"The resulting frequency is {resulting_frequency}")