s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {1, 3}
s4 = {1,2, 3, 4, 5, 6, 7, 8}

s1.add(9)

print(s1)

s1.discard(3)

print(s1)

print(s1.pop())

print(s1)

s1.union(s2)
print(s1 | s2)

#s1.update(s2)
#s1 |= s2

s1.intersection(s2)
print(s1 & s2)

#s1.intersection_update(s2)
#s1 &= s2

print(s1 - s2)
print(s1.difference(s2))

#s1.difference_update(s2)
#s1 -= s2

print(s1 ^ s2)
print(s1.symmetric_difference(s2))

#s1.symmetric_difference_update(s2)
#s1 ^= s2

print(s2.issubset(s4))
print(s1.issuperset(s3))
