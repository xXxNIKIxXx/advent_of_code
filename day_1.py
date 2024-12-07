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