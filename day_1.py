def calculate_fuel(mass):
    return mass // 3 - 2

def total_fuel_requirement(filename):
    total_fuel = 0
    with open(filename, 'r') as file:
        for line in file:
            mass = int(line.strip())
            total_fuel += calculate_fuel(mass)
    return total_fuel

filename = 'day_1.txt'
total_fuel = total_fuel_requirement(filename)
print(f"Total fuel requirement: {total_fuel}")