import requests
from Crypto.Cipher import AES
import hashlib

BASE_URL = "http://aes.cryptohack.org/passwords_as_keys/"

# get the ciphertext
response = requests.get(f"{BASE_URL}/encrypt_flag")
data = response.json()  # key + value
ciphertext = data["ciphertext"]

bytes_ciphertext = bytes.fromhex(ciphertext)
result = ''

with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]

for w in words:
    key = hashlib.md5(w.encode()).digest()

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(bytes_ciphertext)

    if b'crypto' in decrypted:
        result = decrypted
        break

print("Result: ", result.decode('utf-8'))

# output: crypto{k3y5__r__n07__p455w0rdz?}
