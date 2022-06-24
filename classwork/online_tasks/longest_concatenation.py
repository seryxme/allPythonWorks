def longest_concat(s, k):
    concat = []
    temp = []

    count = 0
    i = 0

    while count < len(s) - (k - 1):
        if len(temp) < k:
            temp.append(s[i + count])
            i += 1
        else:
            s1 = "".join(temp)
            concat.append(s1)
            temp = []
            count += 1
            i = 0

    concat.sort(key=len, reverse=True)
    longest_str = concat[0]
    longest = len(concat[0])
    for a in range(len(concat)):
        if len(concat[a]) > longest:
            longest_str = concat[a]

    return longest_str


lst = ["abigail", "theta", "ten", "buga", "tetracycline", "abigail"]
print(longest_concat(lst, 2))
