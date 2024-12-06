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