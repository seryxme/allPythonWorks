import string

alphabets = string.ascii_letters



def encrypt(word, key):

    cypher = word.translate(str.maketrans(alphabets, alphabets[key:] + alphabets[:key]))

    super_cy = cypher.translate(str.maketrans(alphabets, alphabets[key:] + alphabets[:key]))

    return super_cy + "\n"

def decrypt(word, key):
    decypher = word.translate(str.maketrans(alphabets[key:] + alphabets[:key], alphabets))

    super_decy = decypher.translate(str.maketrans(alphabets[key:] + alphabets[:key], alphabets))

    return super_decy + "\n"


print("""
What do you want to do:
1. Encrypt
2. Decrypt
""")

print(encrypt(sender_input, key))


receiver_input = input("Enter a word to decrypt: ")

while not receiver_input.isalpha():
    receiver_input = input("Only alphabets please! Enter a word to encrypt: ")

key2 = input("Enter your key: ")

while not key2.isdigit():
    key2 = input("Only numbers please! Enter your key: ")

key2 = int(key2)

print(decrypt(receiver_input, key2))