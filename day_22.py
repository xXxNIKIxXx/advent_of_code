from typing import List, Optional, Dict, Generator
from dataclasses import dataclass, replace

@dataclass
class Spell:
    name: str
    cost: int
    damage: int
    heal: int
    armor: int
    mana: int
    duration: int

all_spells = [
    Spell(name="Magic Missile", cost=53, damage=4, heal=0, armor=0, mana=0, duration=1),
    Spell(name="Drain", cost=73, damage=2, heal=2, armor=0, mana=0, duration=1),
    Spell(name="Shield", cost=113, damage=0, heal=0, armor=7, mana=0, duration=6),
    Spell(name="Poison", cost=173, damage=3, heal=0, armor=0, mana=0, duration=6),
    Spell(name="Recharge", cost=229, damage=0, heal=0, armor=0, mana=101, duration=5),
]

def play(part: int, my_turn: bool, spent: int, 
         state: Dict[str, int], boss: Dict[str, int], 
         spells: List[Spell]) -> Generator[Optional[int], None, None]:
    hp, mana = state['hp'], state['mana']
    boss_hp, boss_damage = boss['hp'], boss['damage']

    # Part 2, lose HP on player's turn
    if part == 2 and my_turn and hp == 1:
        yield None
        return

    # Apply effects
    mana += sum(s.mana for s in spells)
    damage = sum(s.damage for s in spells)
    armor = sum(s.armor for s in spells)

    # Boss takes effect damage
    boss_hp -= damage
    if boss_hp <= 0:
        yield spent
        return

    # Update spells durations
    spells = [replace(s, duration=s.duration - 1) for s in spells if s.duration > 1]

    if my_turn:
        # Part 2, player loses 1 HP on their turn
        hp = hp - 1 if part == 2 else hp

        # Check available spells
        available_spells = [
            s for s in all_spells
            if s.cost <= mana and not any(s.name == active.name for active in spells)
        ]

        if not available_spells:
            yield None
            return

        # Simulate each possible spell
        for spell in available_spells:
            new_spent = spent + spell.cost
            new_mana = mana - spell.cost
            extra_damage = spell.damage if spell.duration == 1 else 0
            heal = spell.heal

            new_boss_hp = boss_hp - extra_damage
            if new_boss_hp <= 0:
                yield new_spent
            else:
                new_spells = spells[:] if spell.duration == 1 else spells + [spell]
                yield from play(part, False, new_spent, 
                               {'hp': hp + heal, 'mana': new_mana}, 
                               {'hp': new_boss_hp, 'damage': boss_damage},
                               new_spells)
    else:
        # Boss's turn
        damage_taken = max(boss_damage - armor, 1)
        hp -= damage_taken
        if hp <= 0:
            yield None
        else:
            yield from play(part, True, spent, 
                           {'hp': hp, 'mana': mana}, 
                           {'hp': boss_hp, 'damage': boss_damage},
                           spells)

# Initial state
initial_state = {'hp': 50, 'mana': 500}
boss_state = {'hp': 51, 'damage': 10}

# Part 1
part1_result = min(filter(None, play(1, True, 0, initial_state, boss_state, [])))
print(f"Part 1 - min to win: {part1_result}")
