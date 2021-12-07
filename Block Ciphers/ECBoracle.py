import requests
import time
import string

BASE_URL = 'http://aes.cryptohack.org//ecb_oracle/'

total = 32 - 1
alphabet = '_' + '@' + '}' + string.digits + string.ascii_lowercase + string.ascii_uppercase
flag = ''


def encrypt(plaintext):
    response = requests.get(f"{BASE_URL}/encrypt/{plaintext}/")
    data = response.json()  # key + value
    ciphertext = data["ciphertext"]
    return ciphertext


def print_blk(hex_blks, step):
    for i in range(0, len(hex_blks), step):
        print(hex_blks[i:i + step], ' ', end='')
    print()


while True:
    payload = '1' * (total - len(flag))
    print(payload)
    expected = encrypt(payload.encode().hex())
    print('E', '', end='')
    print_blk(expected, 32)

    for c in alphabet:
        res = encrypt(bytes.hex((payload + flag + c).encode()))
        print(c, '', end='')
        print_blk(res, 32)
        if res[32:64] == expected[32:64]:
            flag += c
            print(flag)
            break

    if flag.endswith('}'):
        break

print("Result: ", flag)

# output: crypto{p3n6u1n5_h473_3cb}
