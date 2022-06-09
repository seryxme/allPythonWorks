word = "Hello there."

print(word.upper())
print(word.lower())
print(word.capitalize())
print(word.title())

print(word.find("e"))
print(word.rfind("e"))

print(word.find("c"))
print(word.rfind("c"))

print(word.find("e", 3))
print(word.index("o"))
print(word.rfind("he"))

print(word.startswith("h"))
print(word.swapcase())

print(word.replace("l", "p", 1))

series = "10110010101"

#print(series.replace("1", "2").replace("0", "1").replace("2", "0"))

print(series.translate(series.maketrans("01", "10")))