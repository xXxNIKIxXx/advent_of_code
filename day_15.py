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