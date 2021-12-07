import requests

# Here we are given an encryption function, a decryption function and a function to retrieve flag by checking key.

BASE_URL = 'http://aes.cryptohack.org/lazy_cbc'
ZERO = b'\0' * 16

response = requests.get(f"{BASE_URL}/encrypt/{ZERO.hex()}")
data = response.json()  # key + value
ciphertext = data["ciphertext"]

# This is E_K(K) since our plaintext is 0
bytes_ciphertext = bytes.fromhex(ciphertext)

# This is 0 || E_K(K), which makes 0 be the ciphertext
# which is XOR'd with K after E_K(K) is decrypted.
ciphertext_with_zeros = ZERO + bytes_ciphertext
response = requests.get(f"{BASE_URL}/receive/{ciphertext_with_zeros.hex()}")
data = response.json()  # key + value
ciphertext = data['error'][len('Invalid plaintext: '):]

# Now, we can extract the decrypted output, which is D_K(0) || K, and pull out K.
bytes_ciphertext = bytes.fromhex(ciphertext)
key = bytes_ciphertext[16:]  # K is the second block

response = requests.get(f"{BASE_URL}/get_flag/{key.hex()}")
data = response.json()  # key + value
plaintext = data['plaintext']

result = bytes.fromhex(plaintext).decode()

print("Result: ", result)

# output: crypto{50m3_p30pl3_d0n7_7h1nk_IV_15_1mp0r74n7_?}
