def longest_string(new_list):
    longest = 0
    for x in new_list:
        if len(x) > longest:
            longest = len(x)
            long_string = x
    return long_string


def longest_string2(new_list):
    new_list.sort(key=len)
    return new_list[-1]


fruits = ["apple", "mango", "agbalumo", "orange", "cherry", "pineapple", "water melon", "cucumber", "banana"]

print(longest_string(fruits))

print(longest_string2(fruits))