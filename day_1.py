def solve_captcha(captcha):
    total = 0
    length = len(captcha)
    for i in range(length):
        if captcha[i] == captcha[(i + 1) % length]:
            total += int(captcha[i])
    return total

with open('day_1.txt', 'r') as file:
    captcha = file.read().strip()
result = solve_captcha(captcha)
print(f"The solution to the captcha is: {result}")

def solve_captcha_part_two(captcha):
    total = 0
    length = len(captcha)
    step = length // 2
    for i in range(length):
        if captcha[i] == captcha[(i + step) % length]:
            total += int(captcha[i])
    return total

result_part_two = solve_captcha_part_two(captcha)
print(f"The solution to the new captcha is: {result_part_two}")