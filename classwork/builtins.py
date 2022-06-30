from functools import reduce

lst = [1, 2, 3, 4, 5, 8]

print(all(True if i >= 7 else False for i in lst))

print(any(True if i >= 7 else False for i in lst))

print(max(["I", "love", "Lovie"], key=len))

m_l = map(lambda x: x**2, lst)

print(list(m_l))

print(list(m_l))

list_of_dict = [{"name": "Asake", "gender": "F"}, {"name": "Boyo", "gender": "M"}]

m_l_d = list(map(lambda x: ("Mr. " if x["gender"] == "M" else "Mrs. ") + x["name"], list_of_dict))

print(m_l_d)

print([("Mr. " if x["gender"] == ["M"] else "Mrs. ") + x["name"] for x in list_of_dict])

f_l_d = list(filter(lambda x: x["gender"] == "M", list_of_dict))

print(f_l_d)
print([name for name in list_of_dict if name["gender"] == "F"])

sum_reduce = reduce(lambda acc, val: acc + val, lst, 100)

print(sum_reduce)

fruits = ["apple", "mango", "agbalumo", "orange", "cherry", "pineapple", "water melon", "cucumber", "banana"]

print(reduce(lambda x, y: x if len(x) <= len(y) else y, fruits))