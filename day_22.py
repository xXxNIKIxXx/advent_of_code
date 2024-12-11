"""
--- Day 22: Wizard Simulator 20XX ---
Little Henry Case decides that defeating bosses with swords and stuff is boring. Now he's playing the game with a wizard. Of course, he gets stuck on another boss and needs your help again.

In this version, combat still proceeds with the player and the boss taking alternating turns. The player still goes first. Now, however, you don't get any equipment; instead, you must choose one of your spells to cast. The first character at or below 0 hit points loses.

Since you're a wizard, you don't get to wear armor, and you can't attack normally. However, since you do magic damage, your opponent's armor is ignored, and so the boss effectively has zero armor as well. As before, if armor (from a spell, in this case) would reduce damage below 1, it becomes 1 instead - that is, the boss' attacks always deal at least 1 damage.

On each of your turns, you must select one of your spells to cast. If you cannot afford to cast any spell, you lose. Spells cost mana; you start with 500 mana, but have no maximum limit. You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
Effects all work the same way. Effects apply at the start of both the player's turns and the boss' turns. Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one. If this decreases the timer to zero, the effect ends. You cannot cast a spell that would start an effect which is already active. However, effects can be started on the same turn they end.

For example, suppose the player has 10 hit points and 250 mana, and that the boss has 13 hit points and 8 damage:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 13 hit points
Player casts Poison.

-- Boss turn --
- Player has 10 hit points, 0 armor, 77 mana
- Boss has 13 hit points
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 damage.

-- Player turn --
- Player has 2 hit points, 0 armor, 77 mana
- Boss has 10 hit points
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 2 hit points, 0 armor, 24 mana
- Boss has 3 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
Now, suppose the same initial conditions, except that the boss has 14 hit points instead:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 14 hit points
Player casts Recharge.

-- Boss turn --
- Player has 10 hit points, 0 armor, 21 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 4.
Boss attacks for 8 damage!

-- Player turn --
- Player has 2 hit points, 0 armor, 122 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 3.
Player casts Shield, increasing armor by 7.

-- Boss turn --
- Player has 2 hit points, 7 armor, 110 mana
- Boss has 14 hit points
Shield's timer is now 5.
Recharge provides 101 mana; its timer is now 2.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 211 mana
- Boss has 14 hit points
Shield's timer is now 4.
Recharge provides 101 mana; its timer is now 1.
Player casts Drain, dealing 2 damage, and healing 2 hit points.

-- Boss turn --
- Player has 3 hit points, 7 armor, 239 mana
- Boss has 12 hit points
Shield's timer is now 3.
Recharge provides 101 mana; its timer is now 0.
Recharge wears off.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 2 hit points, 7 armor, 340 mana
- Boss has 12 hit points
Shield's timer is now 2.
Player casts Poison.

-- Boss turn --
- Player has 2 hit points, 7 armor, 167 mana
- Boss has 12 hit points
Shield's timer is now 1.
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 167 mana
- Boss has 9 hit points
Shield's timer is now 0.
Shield wears off, decreasing armor by 7.
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 1 hit point, 0 armor, 114 mana
- Boss has 2 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
You start with 50 hit points and 500 mana points. The boss's actual stats are in your puzzle input. What is the least amount of mana you can spend and still win the fight? (Do not include mana recharge effects as "spending" negative mana.)

Your puzzle answer was 900.

--- Part Two ---
On the next run through the game, you increase the difficulty to hard.

At the start of each player turn (before any other effects apply), you lose 1 hit point. If this brings you to or below 0 hit points, you lose.

With the same starting stats for you and the boss, what is the least amount of mana you can spend and still win the fight?

Your puzzle answer was 1216.
"""
class Player:
    def __init__(self, initial, is_wizard):
        self.history = []
        self.initial = initial
        self.is_wizard = is_wizard

        if self.is_wizard:
            self.spells = [
                {"cost": 53, "effect": lambda m, o: o.damage(4)},
                {"cost": 73, "effect": lambda m, o: (o.damage(2), setattr(m, 'hp', m.hp + 2))},
                {"cost": 113, "start": lambda m, o: setattr(m, 'armor', m.armor + 7), "effect": lambda m, o: None, "end": lambda m, o: setattr(m, 'armor', m.armor - 7), "duration": 6},
                {"cost": 173, "effect": lambda m, o: o.damage(3), "duration": 6},
                {"cost": 229, "effect": lambda m, o: setattr(m, 'mana', m.mana + 101), "duration": 5}
            ]

        self.start()

    def attack(self, opponent, spell_idx=None):
        if not self.is_wizard:
            opponent.damage(self.damage_amt)
        else:
            spell = self.spells[spell_idx]
            self.history.append(spell_idx)
            self.spent += spell["cost"]
            self.mana -= spell["cost"]

            if "duration" in spell:
                new_spell = {"idx": spell_idx, "effect": spell["effect"], "duration": spell["duration"]}
                if "start" in spell:
                    spell["start"](self, opponent)
                if "end" in spell:
                    new_spell["end"] = spell["end"]
                self.active_spells.append(new_spell)
            else:
                spell["effect"](self, opponent)

    def damage(self, n):
        self.hp -= max(1, n - self.armor)

    def duplicate(self):
        new_player = Player(self.initial, self.is_wizard)
        new_player.hp = self.hp
        new_player.spent = self.spent
        new_player.armor = self.armor
        new_player.turn = self.turn
        new_player.active_spells = [spell.copy() for spell in self.active_spells]
        new_player.history = self.history[:]

        if self.is_wizard:
            new_player.mana = self.mana
        else:
            new_player.damage_amt = self.damage_amt

        return new_player

    def take_turn(self, opponent):
        self.turn += 1

        for spell in self.active_spells:
            if spell["duration"] > 0:
                spell["effect"](self, opponent)
                spell["duration"] -= 1

                if spell["duration"] == 0 and "end" in spell:
                    spell["end"](self, opponent)

    def start(self):
        self.hp = self.initial["hp"]
        self.spent = 0
        self.armor = 0
        self.turn = 0
        self.active_spells = []
        if self.is_wizard:
            self.mana = self.initial["mana"]
        else:
            self.damage_amt = self.initial["damage_amt"]


me = Player({"hp": 50, "mana": 500}, True)
boss = Player({"hp": 51, "damage_amt": 9}, False)
cheapest_spent = float('inf')


def play_all_games(me, boss):
    global cheapest_spent
    for i in range(len(me.spells)):
        spell_match = False

        for spell in me.active_spells:
            if spell["duration"] > 1 and i == spell["idx"]:
                spell_match = True

        if spell_match:
            continue
        if me.spells[i]["cost"] > me.mana:
            continue

        new_me = me.duplicate()
        new_boss = boss.duplicate()

        new_me.take_turn(new_boss)
        new_boss.take_turn(new_me)
        new_me.attack(new_boss, i)

        new_me.take_turn(new_boss)
        new_boss.take_turn(new_me)
        new_boss.attack(new_me)

        if new_boss.hp <= 0:
            cheapest_spent = min(cheapest_spent, new_me.spent)
        if new_me.hp > 0 and new_boss.hp > 0 and new_me.spent < cheapest_spent:
            play_all_games(new_me, new_boss)


play_all_games(me, boss)

print(cheapest_spent)


me = Player({"hp": 50, "mana": 500}, True)
boss = Player({"hp": 51, "damage_amt": 9}, False)
cheapest_spent = float('inf')

def play_all_games(me, boss):
    global cheapest_spent
    for i in range(len(me.spells)):
        spell_match = False

        for spell in me.active_spells:
            if spell["duration"] > 1 and i == spell["idx"]:
                spell_match = True

        if spell_match:
            continue
        if me.spells[i]["cost"] > me.mana:
            continue

        new_me = me.duplicate()
        new_boss = boss.duplicate()

        new_me.hp -= 1  # Hard mode: lose 1 HP at the start of each turn
        if new_me.hp <= 0:
            continue

        new_me.take_turn(new_boss)
        new_boss.take_turn(new_me)
        new_me.attack(new_boss, i)

        new_me.take_turn(new_boss)
        new_boss.take_turn(new_me)
        new_boss.attack(new_me)

        if new_boss.hp <= 0:
            cheapest_spent = min(cheapest_spent, new_me.spent)
        if new_me.hp > 1 and new_boss.hp > 0 and new_me.spent < cheapest_spent:
            play_all_games(new_me, new_boss)

play_all_games(me, boss)

print(cheapest_spent)