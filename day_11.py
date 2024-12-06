def increment_password(password):
    password = list(password)
    for i in range(len(password) - 1, -1, -1):
        if password[i] == 'z':
            password[i] = 'a'
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return ''.join(password)

def has_straight(password):
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i]) + 2 == ord(password[i + 2]):
            return True
    return False

def has_no_confusing_letters(password):
    return all(c not in password for c in 'iol')

def has_two_pairs(password):
    pairs = set()
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs.add(password[i])
            i += 1
        i += 1
    return len(pairs) >= 2

def is_valid_password(password):
    return has_straight(password) and has_no_confusing_letters(password) and has_two_pairs(password)

def find_next_password(password):
    password = increment_password(password)
    while not is_valid_password(password):
        password = increment_password(password)
    return password

current_password = 'hepxcrrq'
next_password = find_next_password(current_password)
print(next_password)