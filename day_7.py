import itertools

# Function to evaluate an expression with operators inserted
def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            result = int(str(result) + str(numbers[i + 1]))  # Concatenate as string and convert to int
    return result

# Function to check if an equation can be true with any operator combination
def is_valid_equation(test_value, numbers, operators):
    possible_operators = list(itertools.product(operators, repeat=len(numbers) - 1))
    
    # Check each combination of operators
    for operator_comb in possible_operators:
        if evaluate_expression(numbers, operator_comb) == test_value:
            return True
    return False

# Function to process the input and compute the total calibration result for any part
def process_equations(filename, operators):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            # Parse the equation into test value and numbers
            test_value_str, numbers_str = line.split(':')
            test_value = int(test_value_str.strip())
            numbers = list(map(int, numbers_str.strip().split()))
            
            # Check if this equation can be made true
            if is_valid_equation(test_value, numbers, operators):
                total += test_value
    
    return total

# Part One: Only + and *
operators_part_one = ['+', '*']
# Part Two: +, * and ||
operators_part_two = ['+', '*', '||']

# Use the filename 'day_7.txt' to process the equations for Part One and Part Two
total_calibration_result_part_one = process_equations('day_7.txt', operators_part_one)
total_calibration_result_part_two = process_equations('day_7.txt', operators_part_two)

print("Part One Total Calibration Result:", total_calibration_result_part_one)
print("Part Two Total Calibration Result:", total_calibration_result_part_two)
