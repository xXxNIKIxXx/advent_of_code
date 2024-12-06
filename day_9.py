import itertools

def parse_input(file_path):
    distances = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' = ')
            distance = int(parts[1])
            locations = parts[0].split(' to ')
            loc1, loc2 = locations[0], locations[1]
            if loc1 not in distances:
                distances[loc1] = {}
            if loc2 not in distances:
                distances[loc2] = {}
            distances[loc1][loc2] = distance
            distances[loc2][loc1] = distance
    return distances

def calculate_route_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    return total_distance

def find_shortest_route(distances):
    locations = list(distances.keys())
    shortest_distance = float('inf')
    for route in itertools.permutations(locations):
        distance = calculate_route_distance(route, distances)
        if distance < shortest_distance:
            shortest_distance = distance
    return shortest_distance

distances = parse_input('day_9.txt')
shortest_distance = find_shortest_route(distances)
print(f"The shortest distance is {shortest_distance}")