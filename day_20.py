"""
--- Day 20: Infinite Elves and Infinite Houses ---
To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on.

Each Elf is assigned a number, too, and delivers presents to houses based on that number:

The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....
There are infinitely many Elves, numbered starting with 1. Each Elf delivers presents equal to ten times his or her number at each house.

So, the first nine houses on the street end up like this:

House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.
The first house gets 10 presents: it is visited only by Elf 1, which delivers 1 * 10 = 10 presents. The fourth house gets 70 presents, because it is visited by Elves 1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.

What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?

Your puzzle answer was 776160.

--- Part Two ---
The Elves decide they don't want to visit an infinite number of houses. Instead, each Elf will stop after delivering presents to 50 houses. To make up for it, they decide to deliver presents equal to eleven times their number at each house.

With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?

Your puzzle answer was 786240.
"""
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