"""
--- Day 16: Aunt Sue ---
Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

children, by human DNA age analysis.
cats. It doesn't differentiate individual breeds.
Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
goldfish. No other kinds of fish.
trees, all in one group.
cars, presumably by exhaust or gasoline or something.
perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?

Your puzzle answer was 213.

--- Part Two ---
As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?

Your puzzle answer was 323.
"""
# Read the MFCSAM analysis
mfcsam_analysis = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

# Read the list of Aunt Sues from the file
aunt_sues = []
with open('day_16.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(': ', 1)
        sue_number = int(parts[0].split()[1])
        attributes = parts[1].split(', ')
        sue_info = {}
        for attribute in attributes:
            key, value = attribute.split(': ')
            sue_info[key] = int(value)
        aunt_sues.append((sue_number, sue_info))

# Determine which Aunt Sue gave the gift
def matches_analysis(sue_info, analysis):
    for key, value in sue_info.items():
        if key in analysis and analysis[key] != value:
            return False
    return True

for sue_number, sue_info in aunt_sues:
    if matches_analysis(sue_info, mfcsam_analysis):
        print(f"Aunt Sue {sue_number} gave you the gift.")
        break
    

def matches_analysis_part_two(sue_info, analysis):
    for key, value in sue_info.items():
        if key in analysis:
            if key in ["cats", "trees"]:
                if value <= analysis[key]:
                    return False
            elif key in ["pomeranians", "goldfish"]:
                if value >= analysis[key]:
                    return False
            else:
                if value != analysis[key]:
                    return False
    return True

for sue_number, sue_info in aunt_sues:
    if matches_analysis_part_two(sue_info, mfcsam_analysis):
        print(f"The real Aunt Sue is {sue_number}.")
        break