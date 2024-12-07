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

def find_first_repeated_frequency(changes):
    frequency = 0
    seen_frequencies = set([frequency])
    while True:
        for change in changes:
            frequency += change
            if frequency in seen_frequencies:
                return frequency
            seen_frequencies.add(frequency)

first_repeated_frequency = find_first_repeated_frequency(changes)
print(f"The first frequency reached twice is {first_repeated_frequency}")