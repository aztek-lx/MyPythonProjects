import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
vigenere_key = []

def alt_swap(text):
    if len(text) % 2 != 0:
        text += ' '
    evens = text[0::2]
    odds = text[1::2]
    out = ''
    for idx in range(len(evens)):
        out += odds[idx] + evens[idx]
    return out

def split_swap(text):
    if len(text) % 2 != 0:
        text += ' '
    mid = int(len(text) / 2)
    part1 = text[0:mid]
    part2 = text[mid:]
    return part2 + part1

def invert(text):
    return text[::-1]

def split_swap_invert(text):
    return invert(split_swap(text))

def invert_split_swap(text):
    return split_swap(invert(text))

def invert_words(text):
    chunks = text.split(' ')
    out = ''
    for word in chunks:
        out += invert(word) + ' '
    return out

def shift_cipher(text, shift_val):
    out = ''
    for char in text:
        if char == ' ':
            out += ' '
        else:
            pos = alphabet.find(char)
            new_pos = (pos + shift_val) % 26
            out += alphabet[new_pos]
    return out

def mirror_cipher(text):
    out = ''
    for char in text:
        if char == ' ':
            out += ' '
        else:
            pos = alphabet.find(char)
            new_pos = 25 - pos
            out += alphabet[new_pos]
    return out

def poly_cipher(text, key):
    out = ''
    for idx, char in enumerate(text):
        if char == ' ':
            out += ' '
        else:
            pos = alphabet.find(char)
            new_pos = (pos + key[idx % len(key)]) % 26
            out += alphabet[new_pos]
    return out

def poly_cipher_decode(text, key):
    dkey = [0] * len(key)
    for idx in range(len(key)):
        dkey[idx] = 26 - key[idx]
    
    out = ''
    for idx, char in enumerate(text):
        if char == ' ':
            out += ' '
        else:
            pos = alphabet.find(char)
            new_pos = (pos + dkey[idx % len(dkey)]) % 26
            out += alphabet[new_pos]
    return out

print()
print()

base_msg = 'one plus one is equal to two'
rand_part = ''

for _ in range(10):
    rand_pos = random.randint(0, 25)
    rand_part += alphabet[rand_pos]

full_msg = base_msg + rand_part

counter = 1
vigenere_key = []
while counter < 5:
    val = random.randint(0, 10)
    vigenere_key.append(val)
    counter += 1

decider = random.randint(0, 1)
if decider == 0:
    encoded_msg = shift_cipher(full_msg, random.randint(1, 25))
else:
    encoded_msg = poly_cipher(full_msg, vigenere_key)

choice = 0
choice = random.randint(0, 4)
if choice == 0:
    encrypted_target = encoded_msg
elif choice == 1:
    encrypted_target = alt_swap(encoded_msg)
elif choice == 2:
    encrypted_target = invert(encoded_msg)
elif choice == 3:
    encrypted_target = split_swap(encoded_msg)
else:
    encrypted_target = mirror_cipher(encoded_msg)

print()
print('I am hearing ...')
print(encrypted_target)
print()

found = False

possible_msgs = [
    encrypted_target,
    alt_swap(encrypted_target),
    invert(encrypted_target),
    split_swap(encrypted_target),
    mirror_cipher(encrypted_target)
]

msg_length = len(base_msg)

for possible_msg in possible_msgs:
    for shift_num in range(1, 26):
        decoded = shift_cipher(possible_msg, shift_num)
        if decoded[:msg_length] == base_msg:
            print('code cracked ...')
            print('Secret code is ...')
            print(decoded[:msg_length])
            found = True
            break
    if found:
        break

if not found:
    for possible_msg in possible_msgs:
        decoded = poly_cipher_decode(possible_msg, vigenere_key)
        if decoded[:msg_length] == base_msg:
            print('code cracked ...')
            print('Secret code is ...')
            print(decoded[:msg_length])
            found = True
            break