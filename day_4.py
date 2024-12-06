import hashlib

def mine_adventcoins(secret_key, startwith):
    number = 1
    while True:
        hash_input = f"{secret_key}{number}".encode()
        hash_output = hashlib.md5(hash_input).hexdigest()
        if hash_output.startswith(startwith):
            return number
        number += 1

secret_key = "yzbqklnj"
result_five = mine_adventcoins(secret_key, "00000")
print(f"The lowest number that produces an MD5 hash starting with five zeroes is: {result_five}")
