def is_nice_string(s):
    vowels = set('aeiou')
    forbidden = ['ab', 'cd', 'pq', 'xy']

    # Check for forbidden substrings
    for f in forbidden:
        if f in s:
            return False

    # Check for at least three vowels
    vowel_count = sum(1 for char in s if char in vowels)
    if vowel_count < 3:
        return False

    # Check for at least one letter that appears twice in a row
    has_double_letter = any(s[i] == s[i + 1] for i in range(len(s) - 1))
    if not has_double_letter:
        return False

    return True

def count_nice_strings(strings):
    return sum(1 for s in strings if is_nice_string(s))


with open('2015/day_5.txt') as f:
    strings = f.read().splitlines()
print(count_nice_strings(strings))