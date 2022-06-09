import string

alphabets = string.ascii_letters

print(alphabets)

sender_input = input("Enter a word to encrypt: ")

while not sender_input.isalpha():
    sender_input = input("Only alphabets please! Enter a word to encrypt: ")

key = input("Enter your key: ")

while not key.isdigit():
    key = input("Only numbers please! Enter your key: ")

key = int(key)

cypher = sender_input.translate(str.maketrans(alphabets, alphabets[key:] + alphabets[:key]))

super_cy = cypher.translate(str.maketrans(alphabets, alphabets[key:] + alphabets[:key]))

print(super_cy + "\n")

receiver_input = input("Enter a word to decrypt: ")

while not receiver_input.isalpha():
    receiver_input = input("Only alphabets please! Enter a word to encrypt: ")

key2 = input("Enter your key: ")

while not key2.isdigit():
    key2 = input("Only numbers please! Enter your key: ")

key2 = int(key2)

decypher = receiver_input.translate(str.maketrans(alphabets[key2:] + alphabets[:key2], alphabets))

super_decy = decypher.translate(str.maketrans(alphabets[key2:] + alphabets[:key2], alphabets))

print(super_decy)