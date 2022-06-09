user_input = input("Enter a five digit number: ")

while len(user_input) != 5:
    user_input = input("Invalid input.\nPlease enter a five digit number: ")

rev_input = user_input[ : :-1]

if rev_input == user_input:
    print(user_input, " is a palindrome.")
else:
    print(user_input, " is not a palindrome.")