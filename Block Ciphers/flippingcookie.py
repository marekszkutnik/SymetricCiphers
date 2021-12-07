import requests
from Crypto.Util.strxor import strxor

BASE_URL = 'https://aes.cryptohack.org/flipping_cookie'

text = b'admin=False;expi'
forge_text = b'admin=True;expir'

# get cookie
response = requests.get(f"{BASE_URL}/get_cookie")
data = response.json()
cookie = data["cookie"]

iv = bytes.fromhex(cookie[:32])

# xor
xor_result = strxor(iv, text)
forge_iv = strxor(xor_result, forge_text)
hex_forge_iv = forge_iv.hex()

# get flag
response = requests.get(f"{BASE_URL}/check_admin/{cookie[32:]}/{hex_forge_iv}")
data = response.json()
result = data["flag"]

print("Result: ", result)

# output: crypto{4u7h3n71c4710n_15_3553n714l}
