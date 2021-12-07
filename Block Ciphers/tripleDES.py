import requests
from Crypto.Util.Padding import unpad

BASE_URL = 'http://aes.cryptohack.org/triple_des'

# DES weak keys
key1 = b"\x01\x01\x01\x01\x01\x01\x01\x01"
key2 = b"\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe"

# 3DES weak key = key1||key2
key = key1 + key2

response = requests.get(f"{BASE_URL}/encrypt_flag/{key.hex()}")
data = response.json()
ciphertext = data['ciphertext']

bytes_ciphertext = bytes.fromhex(ciphertext)

response = requests.get(f"{BASE_URL}//encrypt/{key.hex()}/{bytes_ciphertext.hex()}/")
data = response.json()
ciphertext = data['ciphertext']

bytes_ciphertext = bytes.fromhex(ciphertext)

result = unpad(bytes_ciphertext, 8)

print("Result: ", result.decode('utf-8'))

# output: crypto{n0t_4ll_k3ys_4r3_g00d_k3ys}
