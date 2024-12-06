"""
--- Day 9: All in a Single Night ---
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

Your puzzle answer was 207.

--- Part Two ---
The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?

Your puzzle answer was 804.
"""
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


def find_longest_route(distances):
    locations = list(distances.keys())
    longest_distance = 0
    for route in itertools.permutations(locations):
        distance = calculate_route_distance(route, distances)
        if distance > longest_distance:
            longest_distance = distance
    return longest_distance

distances = parse_input('day_9.txt')
shortest_distance = find_shortest_route(distances)
print(f"The shortest distance is {shortest_distance}")

longest_distance = find_longest_route(distances)
print(f"The longest distance is {longest_distance}")