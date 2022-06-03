first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

sum = first_number + second_number + third_number
product = first_number * second_number * third_number
average = sum / 3

print("The sum of the numbers is", sum)
print("The product of the numbers is", product)
print("The average of the numbers is", average)

if first_number > second_number > third_number:
    largest_number = first_number

if first_number > third_number > second_number:
    largest_number = first_number

if second_number > first_number > third_number:
    largest_number = second_number

if second_number > third_number > first_number:
    largest_number = second_number

print(largest_number, "is the largest number.")

