import itertools

# Function to evaluate an expression with operators inserted
def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
    return result

# Function to check if an equation can be true
def is_valid_equation(test_value, numbers):
    # Generate all possible combinations of '+' and '*' for the given numbers
    possible_operators = list(itertools.product(['+', '*'], repeat=len(numbers) - 1))
    
    # Check each combination of operators
    for operators in possible_operators:
        if evaluate_expression(numbers, operators) == test_value:
            return True
    return False

# Function to process the input and compute the total calibration result
def process_equations(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            # Parse the equation into test value and numbers
            test_value_str, numbers_str = line.split(':')
            test_value = int(test_value_str.strip())
            numbers = list(map(int, numbers_str.strip().split()))
            
            # Check if this equation can be made true
            if is_valid_equation(test_value, numbers):
                total += test_value
    
    return total

# Use the filename 'day_7.txt' to process the equations
total_calibration_result = process_equations('day_7.txt')
print("Total Calibration Result:", total_calibration_result)
