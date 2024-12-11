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


def part2(input_str):
    num_of_presents = int(input_str)
    presents_per_house = 11
    max_deliveries_per_elf = 50

    def elves_who_visited(house_no):
        """Return a list of elves that visit a given house."""
        elves = set()
        for elf in range(1, int(house_no**0.5) + 1):
            if house_no % elf == 0:
                elves.add(elf)
                elves.add(house_no // elf)
        return list(elves)

    house_no = 1
    while True:
        # Filter elves based on the delivery limit
        elves = [elf for elf in elves_who_visited(house_no) if house_no // elf <= max_deliveries_per_elf]
        # Calculate total presents delivered to this house
        total_presents = sum(elves) * presents_per_house
        if total_presents >= num_of_presents:
            break
        house_no += 1

    return house_no

print(part2("33100000"))