def count_increases(depths):
    increases = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increases += 1
    return increases

with open('day_1.txt', 'r') as file:
    depths = [int(line.strip()) for line in file.readlines()]

result = count_increases(depths)
print(f"Number of increases: {result}")

def count_window_increases(depths):
    window_sums = [sum(depths[i:i+3]) for i in range(len(depths) - 2)]
    increases = 0
    for i in range(1, len(window_sums)):
        if window_sums[i] > window_sums[i - 1]:
            increases += 1
    return increases

window_result = count_window_increases(depths)
print(f"Number of sliding window increases: {window_result}")