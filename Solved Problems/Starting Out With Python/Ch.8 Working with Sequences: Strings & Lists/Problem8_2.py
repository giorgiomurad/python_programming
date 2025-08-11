# Problem from Starting Out With Python by Tony Gaddis
# Chapter 8: Working with Sequences: Strings and Lists
#
# Problem 8.2:  Write a program that asks the user to enter a series of single digit numbers
#               with nothing separating them. The program should display the sum of all single
#               digit numbers in the string.
#
#               For example:    If the user enters 2514, the method should return 12, which the sum
#                               of all the digits in the string.
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the series of single digit numbers
numbers = input('Enter a series of single digit numbers: ')

# Using a loop to generate the sum of all digits
sum = 0
for digit in numbers:
    sum += int(digit)

# Displaying the sum of all digits
print('The sum of all digits is', sum)