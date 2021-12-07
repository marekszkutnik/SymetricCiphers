import requests
from pwn import xor

BASE_URL = 'http://aes.cryptohack.org/ecbcbcwtf'

response = requests.get(f"{BASE_URL}/encrypt_flag")
data = response.json()
ciphertext = data["ciphertext"]

bytes_ciphertext = bytes.fromhex(ciphertext)
cipher_blocks = [bytes_ciphertext[i:i + 16] for i in range(0, len(bytes_ciphertext), 16)]

response = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = response.json()
plaintext = data["plaintext"]

bytes_plaintext = bytes.fromhex(plaintext)
msg_blocks = [bytes_plaintext[i:i + 16] for i in range(0, len(bytes_plaintext), 16)]

part1 = (xor(msg_blocks[1], cipher_blocks[0]))
part2 = (xor(msg_blocks[2], cipher_blocks[1]))

result = (part1 + part2).decode()

print("Result: ", result)

# output: crypto{3cb_5uck5_4v01d_17_!!!!!}
