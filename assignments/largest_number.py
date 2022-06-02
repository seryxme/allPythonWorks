first_number = input("Enter one number: ")
second_number = input("Enter another number: ")

if first_number > second_number:
    print(first_number,"is larger than", second_number)
elif second_number > first_number:
    print(second_number,"is larger than", first_number)
else:
    print("Both numbers are equal")