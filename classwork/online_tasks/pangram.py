import string

def is_pangram(s):
    alph = string.ascii_lowercase
    s = s.lower()

    return set(alph) <= set(s)


print(is_pangram("A quick brown fox jumps over the lazy dog."))