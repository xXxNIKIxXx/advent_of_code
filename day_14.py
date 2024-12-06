import re

def parse_reindeer_data(file_path):
    reindeer = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)
            if match:
                name, speed, fly_time, rest_time = match.groups()
                reindeer.append({
                    'name': name,
                    'speed': int(speed),
                    'fly_time': int(fly_time),
                    'rest_time': int(rest_time)
                })
    return reindeer

def calculate_distance(reindeer, total_time):
    cycle_time = reindeer['fly_time'] + reindeer['rest_time']
    full_cycles = total_time // cycle_time
    remaining_time = total_time % cycle_time
    fly_time = min(reindeer['fly_time'], remaining_time)
    distance = (full_cycles * reindeer['fly_time'] + fly_time) * reindeer['speed']
    return distance

def find_winning_reindeer(file_path, total_time):
    reindeer_data = parse_reindeer_data(file_path)
    distances = {r['name']: calculate_distance(r, total_time) for r in reindeer_data}
    winning_reindeer = max(distances, key=distances.get)
    return winning_reindeer, distances[winning_reindeer]

file_path = 'day_14.txt'
total_time = 2503
winner, distance = find_winning_reindeer(file_path, total_time)
print(f"The winning reindeer is {winner} with a distance of {distance} km.")