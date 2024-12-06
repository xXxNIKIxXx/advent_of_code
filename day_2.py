with open("2015/day_2.txt") as f:
    lines = f.readlines()

total_paper = 0

for line in lines:
    line = line.replace("\n", "")
    l, w, h = map(int, line.split('x'))
    side1 = l * w
    side2 = w * h
    side3 = h * l
    smallest_side = min(side1, side2, side3)
    surface_area = 2 * side1 + 2 * side2 + 2 * side3
    total_paper += surface_area + smallest_side

print(f"Total wrapping paper needed: {total_paper} square feet")