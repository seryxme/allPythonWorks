d1 = {'a': 1, 'b': 2, 'c': 3}

# d1.pop('a')
# print(d1)

d1.popitem()
print(d1)

d1.update({'d': 4, 'f': 6})
print(d1)

print(d1.items())

print(d1.keys())
print(d1.values())

print(d1.get('g', "Not in dictionary"))