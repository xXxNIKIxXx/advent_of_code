"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

Your puzzle answer was 987339.

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

Your puzzle answer was 259521570.
"""
def find_entries_sum_to_2020(expense_report):
    entries = set()
    for number in expense_report:
        target = 2020 - number
        if target in entries:
            return number, target
        entries.add(number)
    return None, None

with open('day_1.txt', 'r') as file:
    expense_report = [int(line.strip()) for line in file.readlines()]

num1, num2 = find_entries_sum_to_2020(expense_report)
if num1 is not None and num2 is not None:
    result = num1 * num2
    print(f"The two entries that sum to 2020 are {num1} and {num2}.")
    print(f"Their product is {result}.")
else:
    print("No entries found that sum to 2020.")

def find_three_entries_sum_to_2020(expense_report):
    for i in range(len(expense_report)):
        entries = set()
        current_sum = 2020 - expense_report[i]
        for j in range(i + 1, len(expense_report)):
            if current_sum - expense_report[j] in entries:
                return expense_report[i], expense_report[j], current_sum - expense_report[j]
            entries.add(expense_report[j])
    return None, None, None

num1, num2, num3 = find_three_entries_sum_to_2020(expense_report)
if num1 is not None and num2 is not None and num3 is not None:
    result = num1 * num2 * num3
    print(f"The three entries that sum to 2020 are {num1}, {num2}, and {num3}.")
    print(f"Their product is {result}.")
else:
    print("No entries found that sum to 2020.")