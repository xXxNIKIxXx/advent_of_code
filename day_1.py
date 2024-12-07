def read_calories(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n\n')
    return [list(map(int, group.split())) for group in lines]

def find_max_calories(calories_list):
    return max(sum(calories) for calories in calories_list)

calories_list = read_calories('day_1.txt')
max_calories = find_max_calories(calories_list)
print(f"The Elf carrying the most Calories has {max_calories} Calories.")

def find_top_three_calories(calories_list):
    sorted_calories = sorted([sum(calories) for calories in calories_list], reverse=True)
    return sum(sorted_calories[:3])

top_three_calories = find_top_three_calories(calories_list)
print(f"The total Calories carried by the top three Elves is {top_three_calories} Calories.")