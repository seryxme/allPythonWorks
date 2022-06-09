def anagram(num):
    if num == 1:
        decision = f"{num} is an anagram."
    else:
        num_sq = num ** 2

        new_num = str(num_sq)

        length = len(new_num)

        last_digits = num_sq % 10 ** (length - 1)

        if num == last_digits:
            decision = f"{num} is an anagram."
        else:
            decision = f"{num} is not an anagram."

    return decision


#num = int(input("Enter a number: "))
for number in range(1, 1001):
    print(f"{number:>4d} squared is {number**2:<5d}")
    print(anagram(number))
