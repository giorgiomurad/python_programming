# Problem from Starting Out With Python by Tony Gaddis
# Chapter 3: Simple Functions
#
# Problem 3.1:  Write a program that prompts the user to enter a distance in kilometers,
#               and converts the distance to miles before displaying it.
#
#               The formula to convert kilometers to miles is as follows:
#                   M = K x 0.6214
#
#
# Author: Giorgio Murad Murad
KILOMETERS_TO_MILES = 0.6214

def kmToMiles(km):
    miles = km * KILOMETERS_TO_MILES
    print(km, 'kilometers is', miles, 'miles')

kilometers = float(input('Enter the distance in kilometers: '))
kmToMiles(kilometers)