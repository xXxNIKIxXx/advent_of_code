"""
--- Day 15: Science for Hungry People ---
Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)
You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76
Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?

Your puzzle answer was 222870.

--- Part Two ---
Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?

Your puzzle answer was 117936.
"""
import itertools

def parse_ingredients(file_path):
    ingredients = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(': ')
            name = parts[0]
            properties = parts[1].split(', ')
            ingredients[name] = {}
            for prop in properties:
                prop_name, value = prop.split(' ')
                ingredients[name][prop_name] = int(value)
    return ingredients

def calculate_score(ingredients, amounts):
    capacity = durability = flavor = texture = 0
    for ingredient, amount in zip(ingredients, amounts):
        capacity += ingredients[ingredient]['capacity'] * amount
        durability += ingredients[ingredient]['durability'] * amount
        flavor += ingredients[ingredient]['flavor'] * amount
        texture += ingredients[ingredient]['texture'] * amount

    if capacity < 0:
        capacity = 0
    if durability < 0:
        durability = 0
    if flavor < 0:
        flavor = 0
    if texture < 0:
        texture = 0

    return capacity * durability * flavor * texture

def find_best_score(ingredients):
    best_score = 0
    for amounts in itertools.product(range(101), repeat=len(ingredients)):
        if sum(amounts) == 100:
            score = calculate_score(ingredients, amounts)
            if score > best_score:
                best_score = score
    return best_score

ingredients = parse_ingredients('day_15.txt')
best_score = find_best_score(ingredients)
print(f"The highest-scoring cookie has a score of: {best_score}")

def calculate_calories(ingredients, amounts):
    calories = 0
    for ingredient, amount in zip(ingredients, amounts):
        calories += ingredients[ingredient]['calories'] * amount
    return calories

def find_best_score_with_calories(ingredients, target_calories):
    best_score = 0
    for amounts in itertools.product(range(101), repeat=len(ingredients)):
        if sum(amounts) == 100:
            if calculate_calories(ingredients, amounts) == target_calories:
                score = calculate_score(ingredients, amounts)
                if score > best_score:
                    best_score = score
    return best_score

best_score_with_calories = find_best_score_with_calories(ingredients, 500)
print(f"The highest-scoring cookie with 500 calories has a score of: {best_score_with_calories}")