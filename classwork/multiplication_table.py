import itertools

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#for x in numbers:
#    for number in numbers:
#        product = x * number
 #       print(f"{number:<4d} X {x:4d} = {product:>4}")
#    print()


#for x in range(1, 13):
 #   for number in range(1, 13):
  #      product = x * number
   #     print(f"{number:<4d} X {x:4d} = {product:>4}")
    #print()

for x in range(1, 13):
    for number in range(1, 13):
        print("{:<4d} X {:4d} = {:>4}".format(number, x, x * number), end="       ")
    print()