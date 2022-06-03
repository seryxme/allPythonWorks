import random

a = "ROCK"
b = "PAPER"
c = "SCISSORS"

rounds = int(input("How many rounds would you like to play?(3, 5, 7): "))

player_score = 0
computer_score = 0
counter = 0

while counter < rounds:
    player = int(input("""
    Choose your option:
    1. ROCK
    2. PAPER
    3. SCISSORS
    """))
    if player == 1:
        print("You chose", a)
    elif player == 2:
        print("You chose", b)
    elif player == 3:
        print("You chose", c)
    else:
        print("Invalid option.")

    option = int(input("""
    1. Done
    0. Exit
    """))

    a_i = random.randint(1, 3)
    if option == 1:
        if a_i == 1:
            print("Computer chose", a)
        elif a_i == 2:
            print("Computer chose", b)
        else:
            print("Computer chose", c)
    else:
        print("Sorry to see you go. Goodbye!")
        break

    if player == a_i:
        print("No winner this round, go again?")
    elif (player == 1 and a_i == 2) or (player == 2 and a_i == 3) or (player == 3 and a_i == 1):
        print("You lose!")
        computer_score += 1
        counter += 1
    else:
        print("You win!")
        player_score += 1
        counter += 1

    print("\nGame score:\nComputer -", computer_score,":", player_score, "- You")

    if (player_score == (rounds//2 + 1)) or (computer_score == (rounds//2 + 1)):
        counter = rounds


else:
    if computer_score > player_score:
        print("\nYou lost the game! Better luck next time!")
    elif computer_score < player_score:
        print("\nYou won the game! you're a master at this!")
    else:
        print("\nAlas! No winner! You're as good as the AI.")
