def get_code(row, col):
    n = (row + col - 2) * (row + col - 1) // 2 + col

    code = 20151125

    for _ in range(n - 1):
        code = (code * 252533) % 33554393

    return code


row = 2978
col = 3083

code = get_code(row, col)

print(f'The code for row {row}, column {col} is {code}')