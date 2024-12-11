def sum_of_divisors(n):
    """Calculate the sum of all divisors of n."""
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sum(divisors)

def find_lowest_house(target_presents):
    """Find the lowest house number to get at least target_presents."""
    house = 1
    while True:
        # Calculate total presents for the current house
        total_presents = 10 * sum_of_divisors(house)
        if total_presents >= target_presents:
            return house
        house += 1

# Puzzle input
target_presents = 33100000
result = find_lowest_house(target_presents)
print(f"The lowest house number to get at least {target_presents} presents is {result}.")
