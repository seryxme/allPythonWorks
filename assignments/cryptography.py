def encryption(number):
    count = 3
    new_num = 0
    for digit in number:

        encode = ((int(digit) + 7) % 10) * 10**count
        new_num += encode
        count -= 1
        new_num = str(new_num)

    return new_num

num = input("Enter a four digit number to encrypt: ")

encrypt = encryption(num)

print(f"{encrypt:0>4d}")







