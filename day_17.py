"""
--- Day 17: No Such Thing as Too Much ---
The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

Your puzzle answer was 1638.

--- Part Two ---
While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.

Your puzzle answer was 17.
"""
from itertools import combinations

def count_combinations(containers, target):
    count = 0
    for i in range(1, len(containers) + 1):
        for combo in combinations(containers, i):
            if sum(combo) == target:
                count += 1
    return count


with open('day_17.txt') as f:
    containers = [int(line.strip()) for line in f.readlines()]

target = 150
result = count_combinations(containers, target)
print(f'Total combinations: {result}')

def min_container_combinations(containers, target):
    min_count = float('inf')
    min_combinations = 0
    for i in range(1, len(containers) + 1):
        for combo in combinations(containers, i):
            if sum(combo) == target:
                if i < min_count:
                    min_count = i
                    min_combinations = 1
                elif i == min_count:
                    min_combinations += 1
    return min_combinations

min_combinations = min_container_combinations(containers, target)
print(f'Minimum container combinations: {min_combinations}')