import requests, io
from PIL import Image
from pwn import xor

# every PNG image begins with the following 16 plaintext bytes.
PNG_PREFIX = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'

BASE_URL = 'http://aes.cryptohack.org/bean_counter/encrypt'

response = requests.get(BASE_URL)
data = response.json()
encrypted = data["encrypted"]

bytes_encrypted = bytes.fromhex(encrypted)

# Plaintext = Keystream XOR Ciphertext --> Keystream = Plaintext XOR Ciphertext
keystream = xor(PNG_PREFIX, bytes_encrypted[:16])

# Decrypt the ciphertext using the keystream above
pt = xor(bytes_encrypted, keystream)

image = Image.open(io.BytesIO(pt))

# Reproduce the image with the plaintext bytes
image.save('bean_flag.png')

# output: crypto{hex_bytes_beans}
