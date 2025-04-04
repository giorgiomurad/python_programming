# Problem from Starting Out With Python by Tony Gaddis
# Chapter 6: Value Returning Functions & Modules
#
# Problem 6.10:  Write a program that allows the user to play a game of
#                Rock (1), Paper (2), Scissors (3) against the computer.
#
#
# Author: Giorgio Murad Murad
import random

# Function that takes the choice of the user and computer in a Rock, Paper, Scissors game,
# and returns who the winner is
def game(user, sys):
    p1 = ""
    p2 = ""
    winner = ""

    if user == 1:
        p1 = "Rock"
    elif user == 2:
        p1 = "Paper"
    elif user == 3:
        p1 = "Scissors"
    if sys == 1:
        p2 = "Rock"
    elif sys == 2:
        p2 = "Paper"
    elif sys == 3:
        p2 = "Scissors"

    print(p1, "vs", p2)
    if user == sys:
        winner = "Draw"
    elif user == 1 and sys == 2:
        winner = "Computer"
    elif user == 1 and sys == 3:
        winner = "User"
    elif user == 2 and sys == 1:
        winner = "User"
    elif user == 2 and sys == 3:
        winner = "Computer"
    elif user == 3 and sys == 1:
        winner = "Computer"
    elif user == 3 and sys == 2:
        winner = "User"

    return winner



# Prompting the user to enter the choice of Rock (1), Paper (2), or Scissors (3)
player1 = int(input("Rock (1), Paper (2), or Scissors (3): "))

# Generating the computer's choice
player2 = random.randint(1, 3)

# Calling the function given the choice of the user and computer
result = game(player1, player2)

# Displaying the winner
if result == "Draw":
    print("It's a Draw!")
elif result == "User":
    print("You Win!")
else:
    print("The Computer Wins!")