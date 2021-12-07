import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

# get the ciphertext
response = requests.get(f"{BASE_URL}/encrypt_flag")
data = response.json()  # key + value
ciphertext = data["ciphertext"]
print("ciphertext: ", ciphertext)

# send the ciphertext to the decrypt function
response = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = response.json()  # key + value
plaintext = data["plaintext"]
print("plaintext: ", plaintext)

# convert from hex to ASCII
result = bytes.fromhex(plaintext)
print("Result: ", result.decode('utf-8'))

# output: crypto{bl0ck_c1ph3r5_4r3_f457_!}
