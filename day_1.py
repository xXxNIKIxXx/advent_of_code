def get_calibration_value(line):
    first_digit = next((char for char in line if char.isdigit()), None)
    last_digit = next((char for char in reversed(line) if char.isdigit()), None)
    if first_digit and last_digit:
        return int(first_digit + last_digit)
    return 0

total_sum = 0
with open('day_1.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            total_sum += get_calibration_value(line)
print(f"The sum of all calibration values is: {total_sum}")
