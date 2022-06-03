import random

mysteryNum = random.randint(1, 100)

counter = 0
while counter < 6:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == mysteryNum:
        print("You guessed right!")
        break
    elif guess > mysteryNum:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")
    counter += 1
else:
    print("Sorry, you cannot guess the number, Olodo!")
    print("Mystery number is ", mysteryNum, end='.')