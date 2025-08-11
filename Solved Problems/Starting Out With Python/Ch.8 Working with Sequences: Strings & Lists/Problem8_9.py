# Problem from Starting Out With Python by Tony Gaddis
# Chapter 8: Working with Sequences: Strings and Lists
#
# Problem 8.9:  Write a program that generates a seven-digit lottery number.
#               The program generate seven random numbers with each ranging from zero to nine, and assigns each
#               number to a list.
#               The program should later use a loop to display the contents of the list.
#
#
# Author: Giorgio Murad Murad
import random

# Initializing list of integers
integers = []

# Generating numbers in the loop and adding the generated numbers in the list
for i in range(7):
    temp = random.randint(0, 9)
    integers.append(temp)

# Displaying the contents of the list
print('The generated lottery number is', end=' ')
for digit in integers:
    print(digit, end='')