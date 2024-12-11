from itertools import combinations

# Define the items in the shop
weapons = [
    {"name": "Dagger", "cost": 8, "damage": 4, "armor": 0},
    {"name": "Shortsword", "cost": 10, "damage": 5, "armor": 0},
    {"name": "Warhammer", "cost": 25, "damage": 6, "armor": 0},
    {"name": "Longsword", "cost": 40, "damage": 7, "armor": 0},
    {"name": "Greataxe", "cost": 74, "damage": 8, "armor": 0},
]

armor = [
    {"name": "None", "cost": 0, "damage": 0, "armor": 0},
    {"name": "Leather", "cost": 13, "damage": 0, "armor": 1},
    {"name": "Chainmail", "cost": 31, "damage": 0, "armor": 2},
    {"name": "Splintmail", "cost": 53, "damage": 0, "armor": 3},
    {"name": "Bandedmail", "cost": 75, "damage": 0, "armor": 4},
    {"name": "Platemail", "cost": 102, "damage": 0, "armor": 5},
]

rings = [
    {"name": "None", "cost": 0, "damage": 0, "armor": 0},
    {"name": "Damage +1", "cost": 25, "damage": 1, "armor": 0},
    {"name": "Damage +2", "cost": 50, "damage": 2, "armor": 0},
    {"name": "Damage +3", "cost": 100, "damage": 3, "armor": 0},
    {"name": "Defense +1", "cost": 20, "damage": 0, "armor": 1},
    {"name": "Defense +2", "cost": 40, "damage": 0, "armor": 2},
    {"name": "Defense +3", "cost": 80, "damage": 0, "armor": 3},
]

# Boss stats (updated with provided input)
boss_hp = 103
boss_damage = 9
boss_armor = 2

# Player stats
player_hp = 100

def simulate_battle(player_damage, player_armor):
    player_turns_to_win = (boss_hp + max(1, player_damage - boss_armor) - 1) // max(1, player_damage - boss_armor)
    boss_turns_to_win = (player_hp + max(1, boss_damage - player_armor) - 1) // max(1, boss_damage - player_armor)
    return player_turns_to_win <= boss_turns_to_win

min_cost = float('inf')

# Generate all possible combinations of items
for weapon in weapons:
    for arm in armor:
        for ring1, ring2 in combinations(rings, 2):
            cost = weapon["cost"] + arm["cost"] + ring1["cost"] + ring2["cost"]
            damage = weapon["damage"] + ring1["damage"] + ring2["damage"]
            total_armor = arm["armor"] + ring1["armor"] + ring2["armor"]
            if simulate_battle(damage, total_armor):
                min_cost = min(min_cost, cost)

print(f"The least amount of gold you can spend and still win the fight is: {min_cost}")