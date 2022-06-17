import random

rng = range(1,101, 5)

print(rng)

rng = list(range(1, 101, 5))

print(rng)

rng.append(1000)
print(rng)

rng.extend([3, 5, ])
print(rng)

rng += [4, 6, 8, 10]
print(rng)

rng.insert(2, 9)
print(rng)

popnum = rng.pop()

print(popnum)
print(rng)

popnum = rng.pop(-5)

print(popnum)
print(rng)

rng.remove(1000)

print(rng)

lst = rng.copy()
rng.clear()
print(rng)
print(lst)

random.shuffle(lst)

print(lst)

lst.sort(reverse=True)

print(lst)

fruits = ["apple", "mango", "agbalumo", "orange", "cherry", "pineapple", "water melon", "cucumber", "banana"]
fruits.sort()

print(fruits)

fruits.sort(key=len)

print(fruits)

fruits.sort(key=len, reverse=True)

print(fruits)
