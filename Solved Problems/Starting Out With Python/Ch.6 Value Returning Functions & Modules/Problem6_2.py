# Problem from Starting Out With Python by Tony Gaddis
# Chapter 6: Value Returning Functions & Modules
#
# Problem 6.2:  Write a program that generates a random math question, and asks
#               the user to enter the answer to that question.
#               The program checks and displays whether the user answered correctly
#               or not.
#
#
# Author: Giorgio Murad Murad
import random



# Math Quiz Function that generates a random math question
# Returns true if the user answers correctly
# Otherwise, false is returned
def mathQuiz():
    operators = ['+', '-', '*', '/', '%']

    nb1 = random.randint(1, 100)
    nb2 = random.randint(1, 100)
    operator = random.choice(operators)

    userAns = int(input("What is " + str(nb1) + " " + operator + " " + str(nb2) + "? "))
    if operator == '+':
        sysAns = nb1 + nb2
    elif operator == '-':
        sysAns = nb1 - nb2
    elif operator == '*':
        sysAns = nb1 * nb2
    elif operator == '/':
        sysAns = nb1 // nb2
    else:
        sysAns = nb1 % nb2

    return userAns == sysAns, sysAns


isCorrect, correctAns = mathQuiz()
if isCorrect:
    print("You got it right!")
else:
    print("You got it wrong."
          "\nThe correct answer is " + str(correctAns) + ".")