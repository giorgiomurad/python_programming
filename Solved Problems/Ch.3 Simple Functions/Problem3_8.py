# Problem from Starting Out With Python by Tony Gaddis
# Chapter 3: Simple Functions
#
# Problem 3.8:  There are three seating categories at a stadium.
#                   .At a softball game:    - Class A seats cost $15
#                                           - Class B seats cost $12
#                                           - Class C seats cost $9
#
#               Write a program that asks how many tickets of each class
#               of seats were sold, and then displays the amount of income
#               generated from ticket sales.
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the number of tickets sold for classes A, B, and C
aClass = int(input('Enter the number of tickets sold for seat class A: '))
bClass = int(input('Enter the number of tickets sold for seat class B: '))
cClass = int(input('Enter the number of tickets sold for seat class C: '))


# Function that generates and displays the income with
# the given class name, number of tickets, and the price.
def classIncome(clName, tickets, price):
    income = tickets * price
    print(
        'The income of class {} is ${}'
        .format(clName, income)
    )


# Calling the same function three times, but given different parameters
classIncome('A', aClass, 15)
classIncome('B', bClass, 12)
classIncome('C', cClass, 9)