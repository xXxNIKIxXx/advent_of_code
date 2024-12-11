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
