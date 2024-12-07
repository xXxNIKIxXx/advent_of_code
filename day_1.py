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
