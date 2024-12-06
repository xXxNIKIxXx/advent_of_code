from collections import Counter

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    
    return total_distance

def calculate_similarity_score(left_list, right_list):
    
    right_count = Counter(right_list)
    similarity_score = sum(num * right_count[num] for num in left_list)
    
    return similarity_score

left_list = []
right_list = []

with open('2024/day_1.txt') as file:
    lines = file.readlines()

for line in lines:
    line = line.replace('\n', '')
    left_list_num, right_list_num = [int(num) for num in line.split()]
    left_list.append(left_list_num)
    right_list.append(right_list_num)
    
    
print(calculate_total_distance(left_list, right_list))

print(calculate_similarity_score(left_list, right_list))