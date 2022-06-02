#a = input("Enter a number: ")
#print(a)

mysteryNum = 7
guess = int(input("Guess a number between 1 and 10: "))

if int(guess) == mysteryNum:
    print("You guessed right!")
else:
    print("Try again.")
