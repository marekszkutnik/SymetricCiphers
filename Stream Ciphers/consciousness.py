# RECON:-
# def encrypt():
#     random_line = random.choice(TEXT)
#     cipher = AES.new(KEY, AES.MODE_CTR, counter=Counter.new(128))
#     encrypted = cipher.encrypt(random_line.encode())
#     return {"ciphertext": encrypted.hex()}

# each time encrypt is called, new AES cipher is created with zero counter.
# Means our keystream used to xor will be same each time, as a result of which we will have all the messages encrypted with the same keystream
# So it becomes a classical example of many time pad, if we xor two ciphertexts, we will have the resultant xor of the corresponding plaintexts
# non uniform distribution of message space makes it possible to recover the messages and also the key.
# I did crib based decryption i.e. guessing a crib, and the ciphertext where the crib is supposed to be.
# If the guessed crib is correct, xoring the crib with its ciphertext should give out the key. Testing the key on all other ciphertext,
# we can verify if our crib was indeed correct or not.
# I solved it manually, by guessing the cribs from the decryptions so far
# The first crib we can deduce easily from the flag format i.e. 'crypto{'

import requests

BASE_URL = "https://aes.cryptohack.org/stream_consciousness/encrypt/"
encryptions = []

for i in range(100):  # big enough number to ensure you have all the ciphertexts
    response = requests.get(BASE_URL)
    data = response.json()
    ciphertext = data['ciphertext']
    encryptions.append(ciphertext)

encryptions = list(set(encryptions))  # removing all duplicates, results in a list of 22 encryptions
encryptions = sorted(encryptions, key=lambda x: len(x))  # sorted by length
encryptions = [bytes.fromhex(i) for i in encryptions]  # from hex to bytes

originalList = encryptions


# taking xor of two messages till the length of smaller message
def bytewiseXor(m1, m2):
    xorlen = min(len(m1), len(m2))
    return bytes([m1[i] ^ m2[i] for i in range(xorlen)])


# function to print the decryptions using the crib and j is the ciphertext number for which we guessed the crib is for
def printDecryptions(j, crib):
    for i in range(len(encryptions)):
        print(decryptions[i] + bytewiseXor(crib, bytewiseXor(encryptions[i], encryptions[j])))


crib = b'crypto{'
for i in range(len(encryptions)):
    if all([bytewiseXor(crib, bytewiseXor(encryptions[i], encryptions[j])).decode().isprintable() for j in
            range(len(encryptions))]):
        textNo = i

# textNo=4 so we can se flag is ciphertext 4 lets try printing decryptions
decryptions = [b'' for i in range(len(encryptions))]
decryptions[textNo] += crib
for i in range(len(encryptions)):
    if i != textNo:
        decryptions[i] += bytewiseXor(crib, bytewiseXor(encryptions[i], encryptions[textNo]))

encryptions = [i[len(crib):] for i in encryptions]  # truncating encryptions by length of crib

for i in decryptions:
    print(i)

# Our? Wh
# But I w
# And I s
# Dress-m
# crypto{
# What a
# It can'
# I shall
# Three b
# No, I'l
# As if I
# How pro
# Why do
# I shall
# The ter
# Would I
# Perhaps
# I'm unh
# Love, p
# Dolly w
# These h
# What a
# I'm unhappy seems a vaild message so lets crib with 'appy' and try decryptions and 17 is the ciphertext number
crib = b'appy'
textNo = 17
printDecryptions(textNo, crib)
# b'Our? Why ou'
# b'but I will '
# b'And I shall'
# b'Dress-makin'
# b'crypto{k3y5'
# b'What a nast'
# b"It can't be"
# b'I shall los'
# b'Three boys '
# b"No, I'll go"
# b'As if I had'
# b'How proud a'
# b'Why do they'
# b"I shall, I'"
# b'The terribl'
# b'Would I hav'
# b'Perhaps he '
# b"I'm unhappy"
# b'Love, proba'
# b'Dolly will '
# b'These horse'
# b'What a lot '
decryptions[textNo] += crib
for i in range(len(encryptions)):
    if i != textNo:
        decryptions[i] += bytewiseXor(crib, bytewiseXor(encryptions[i], encryptions[textNo]))

encryptions = [i[len(crib):] for i in encryptions]

# Love probably seems good, so lets try crib 'bly' and ciphertext number 18
textNo = 18
crib = b'bly'
printDecryptions(textNo, crib)
# b'Our? Why our?'
# b'But I will sho'
# b'And I shall ig'
# b'Dress-making a'
# b'crypto{k3y57r3'
# b'What a nasty s'
# b"It can't be to"
# b'I shall lose e'
# b'Three boys run'
# b"No, I'll go in"
# b'As if I had an'
# b'How proud and '
# b'Why do they go'
# b"I shall, I'll "
# b'The terrible t'
# b'Would I have b'
# b'Perhaps he has'
# b"I'm unhappy, I"
# b'Love, probably'
# b'Dolly will thi'
# b'These horses, '
# b'What a lot of '
# cool that worked
decryptions[textNo] += crib
for i in range(len(encryptions)):
    if i != textNo:
        decryptions[i] += bytewiseXor(crib, bytewiseXor(encryptions[i], encryptions[textNo]))

encryptions = [i[len(crib):] for i in encryptions]

# What a nasty smell  so lets try out "mell " as the crib and text no is 5
textNo = 5
crib = b'mell '
printDecryptions(textNo, crib)
# b'Our? Why our?'
# b'But I will show him'
# b'And I shall ignore '
# b'Dress-making and Mi'
# b'crypto{k3y57r34m_r3'
# b'What a nasty smell '
# b"It can't be torn ou"
# b'I shall lose everyt'
# b'Three boys running,'
# b"No, I'll go in to D"
# b'As if I had any wis'
# b'How proud and happy'
# b'Why do they go on p'
# b"I shall, I'll lose "
# b'The terrible thing '
# b'Would I have believ'
# b'Perhaps he has miss'
# b"I'm unhappy, I dese"
# b'Love, probably? The'
# b'Dolly will think th'
# b'These horses, this '
# b'What a lot of thing'
decryptions[textNo] += crib
for i in range(len(encryptions)):
    if i != textNo:
        decryptions[i] += bytewiseXor(crib, bytewiseXor(encryptions[i], encryptions[textNo]))

encryptions = [i[len(crib):] for i in encryptions]
# I shall lose everything, so lets try "hing " and text number 7
textNo = 7
crib = b'hing '
printDecryptions(textNo, crib)
# b'Our? Why our?'
# b'But I will show him.'
# b'And I shall ignore it.'
# b'Dress-making and Millin'
# b'crypto{k3y57r34m_r3u53_'
# b'What a nasty smell this'
# b"It can't be torn out, b"
# b'I shall lose everything'
# b'Three boys running, pla'
# b"No, I'll go in to Dolly"
# b'As if I had any wish to'
# b"How proud and happy he'"
# b'Why do they go on paint'
# b"I shall, I'll lose ever"
# b'The terrible thing is t'
# b'Would I have believed t'
# b'Perhaps he has missed t'
# b"I'm unhappy, I deserve "
# b'Love, probably? They do'
# b'Dolly will think that I'
# b'These horses, this carr'
# b'What a lot of things th'
decryptions[textNo] += crib
for i in range(len(encryptions)):
    if i != textNo:
        decryptions[i] += bytewiseXor(crib, bytewiseXor(encryptions[i], encryptions[textNo]))

encryptions = [i[len(crib):] for i in encryptions]
# I see I shall lose everything again so lets try "thing " as crib and textNo 13
crib = b'thing '
textNo = 13
printDecryptions(textNo, crib)
# b'Our? Why our?'
# b'But I will show him.'
# b'And I shall ignore it.'
# b'Dress-making and Millinery'
# b'crypto{k3y57r34m_r3u53_15_f474'
# b'What a nasty smell this paint '
# b"It can't be torn out, but it c"
# b'I shall lose everything and no'
# b'Three boys running, playing at'
# b"No, I'll go in to Dolly and te"
# b'As if I had any wish to be in '
# b"How proud and happy he'll be w"
# b'Why do they go on painting and'
# b"I shall, I'll lose everything "
# b'The terrible thing is that the'
# b'Would I have believed then tha'
# b'Perhaps he has missed the trai'
# b"I'm unhappy, I deserve it, the"
# b"Love, probably? They don't kno"
# b"Dolly will think that I'm leav"
# b'These horses, this carriage - '
# b'What a lot of things that then'
decryptions[textNo] += crib
for i in range(len(encryptions)):
    if i != textNo:
        decryptions[i] += bytewiseXor(crib, bytewiseXor(encryptions[i], encryptions[textNo]))

encryptions = [i[len(crib):] for i in encryptions]
# I'm leaving , so lets try b'ing ' and text number
textNo = 19
crib = b'ing '
printDecryptions(textNo, crib)
# b'Our? Why our?'
# b'But I will show him.'
# b'And I shall ignore it.'
# b'Dress-making and Millinery'
# b'crypto{k3y57r34m_r3u53_15_f474l}'
# b'What a nasty smell this paint had.'
# b"It can't be torn out, but it can b"
# b'I shall lose everything and not ge'
# b'Three boys running, playing at hor'
# b"No, I'll go in to Dolly and tell h"
# b'As if I had any wish to be in the '
# b"How proud and happy he'll be when "
# b'Why do they go on painting and bui'
# b"I shall, I'll lose everything if h"
# b'The terrible thing is that the pas'
# b'Would I have believed then that I '
# b'Perhaps he has missed the train an'
# b"I'm unhappy, I deserve it, the fau"
# b"Love, probably? They don't know ho"
# b"Dolly will think that I'm leaving "
# b'These horses, this carriage - how '
# b'What a lot of things that then see'
# and we are done :)

# output: crypto{k3y57r34m_r3u53_15_f474l}
