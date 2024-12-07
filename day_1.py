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

sum_part2 = 0

integer_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('day_1.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            nums = []
            for i, letter in enumerate(line):
                for val, name in enumerate(integer_names):
                    if name in line[i:i+len(name)]:
                        nums.append(str(val))
                if letter.isdigit():
                    nums.append(letter)
            if nums:
                sum_part2 += int(nums[0] + nums[-1])

print(f"The sum of all part 2 values is: {sum_part2}")
