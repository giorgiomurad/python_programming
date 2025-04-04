# Problem from Starting Out With Python by Tony Gaddis
# Chapter 6: Value Returning Functions & Modules
#
# Problem 6.3:  Write a program that asks the user for two integer values,
#               and calls a function that returns the maximum between the
#               two values.
#               The program should then display the greater integer value.
#
#
# Author: Giorgio Murad Murad

# Function that returns the maximum of two given integer values
def maximum(a, b):
    if a > b:
        return a
    else:
        return b


# Prompting the user to enter the values of integer 1 and 2
nb1 = int(input("Enter the first integer value: "))
nb2 = int(input("Enter the second integer value: "))

# Calling the function given the two integer values,
# And assigning the returned value to a variable
maxNb = maximum(nb1, nb2)

# Displaying result
print("The maximum integer value is", maxNb)