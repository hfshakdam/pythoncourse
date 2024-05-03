import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()
        #avoids case sensitivity problems
    if player == computer:
        print("You chose",player)
        print("The computer chose",computer)
        print("Tied!")
    elif player == "rock":
        if computer == "paper":
            print("You chose", player)
            print("The computer chose", computer)
            print("You Lose!")
        if computer == "scissors":
            print("You chose", player)
            print("The computer chose", computer)
            print("You Win!")
    elif player == "paper":
        if computer == "scissors":
            print("You chose", player)
            print("The computer chose", computer)
            print("You Lose!")
        if computer == "rock":
            print("You chose", player)
            print("The computer chose", computer)
            print("You Win!")
    elif player == "scissors":
        if computer == "rock":
            print("You chose", player)
            print("The computer chose", computer)
            print("You Lose!")
        if computer == "paper":
            print("You chose", player)
            print("The computer chose", computer)
            print("You Win!")

    play_again = input("Play again? (Yes/No): ").lower()

    if play_again !="yes":
        break

print("Bye!")