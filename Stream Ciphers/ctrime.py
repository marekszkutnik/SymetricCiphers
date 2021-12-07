import time
import requests
import string

BASE_URL = 'http://aes.cryptohack.org/ctrime/encrypt/'

alphabet = '}' + '!' + '_' + '@' + '?' + string.ascii_uppercase + string.digits + string.ascii_lowercase
# flag = b'crypto{'
flag = b'crypto{CRIME'


def print_blk(hex_blks, step):
    for i in range(0, len(hex_blks), step):
        print(hex_blks[i:i + step], ' ', end='')
    print()


def encrypt(plaintext):
    response = requests.get(f"{BASE_URL}/{plaintext}/")
    data = response.json()  # key + value
    ciphertext = data["ciphertext"]
    return ciphertext


ciphertext = encrypt(flag.hex())
mi = len(ciphertext)

while True:
    for c in alphabet:
        ciphertext = encrypt((flag + c.encode()).hex())
        print(c, len(ciphertext))
        if mi == len(ciphertext):
            flag += c.encode()
            mi = len(ciphertext)
            print(mi, flag)
            break
        if c == alphabet[-1]:
            mi += 2
            break

    if flag.endswith(b'}'):
        print(flag)
        break

print("Result: ", flag)

# output: crypto{CRIME_571ll_p4y5}
