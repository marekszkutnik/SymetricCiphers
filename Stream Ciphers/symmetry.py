import requests

BLOCK_SIZE = 16

BASE_URL = 'http://aes.cryptohack.org/symmetry'

response = requests.get(f"{BASE_URL}/encrypt_flag")
data = response.json()
ciphertext = data["ciphertext"]

bytes_ciphertext = bytes.fromhex(ciphertext)

# Split the ciphertext into the IV and the actual ciphertext
ciphertext = bytes_ciphertext[BLOCK_SIZE:]
iv = bytes_ciphertext[:BLOCK_SIZE]

# Encrypt the ciphertext (E_K(IV) ^ FLAG) which just will encrypt the supplied
# IV as E_K(IV) and XOR it with the ciphertext and recover the flag. Abuses
# the fact that encryption and decryption perform the same operation in OFB mode.
response = requests.get(f"{BASE_URL}/encrypt/{ciphertext.hex()}/{iv.hex()}")
data = response.json()
ciphertext = data["ciphertext"]

plaintext = bytes.fromhex(ciphertext)
print("Result: ", plaintext.decode())

# output: crypto{0fb_15_5ymm37r1c4l_!!!11!}
