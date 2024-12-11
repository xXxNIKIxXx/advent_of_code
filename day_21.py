"""
--- Day 21: RPG Simulator 20XX ---
Little Henry Case got a new video game for Christmas. It's an RPG, and he's stuck on a boss. He needs to know what equipment to buy at the shop. He hands you the controller.

In this game, the player (you) and the enemy (the boss) take turns attacking. The player always goes first. Each attack reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points. If the defender had an armor score of 300, the defender would still lose 1 hit point.

Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold. You start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats from all of your items. You have 100 hit points.

Here is what the item shop is selling:

Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand). You must use any items you buy. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:

The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
In this scenario, the player wins! (Barely.)

You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?

Your puzzle answer was 121.

--- Part Two ---
Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants. The other rules still apply, and he still only has one of each item.

What is the most amount of gold you can spend and still lose the fight?

Your puzzle answer was 201.
"""
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

max_cost = 0

# Generate all possible combinations of items
for weapon in weapons:
    for arm in armor:
        for ring1, ring2 in combinations(rings, 2):
            cost = weapon["cost"] + arm["cost"] + ring1["cost"] + ring2["cost"]
            damage = weapon["damage"] + ring1["damage"] + ring2["damage"]
            total_armor = arm["armor"] + ring1["armor"] + ring2["armor"]
            if not simulate_battle(damage, total_armor):
                max_cost = max(max_cost, cost)

print(f"The most amount of gold you can spend and still lose the fight is: {max_cost}")