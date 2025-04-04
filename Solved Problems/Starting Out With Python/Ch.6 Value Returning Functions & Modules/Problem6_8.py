# Problem from Starting Out With Python by Tony Gaddis
# Chapter 6: Value Returning Functions & Modules
#
# Problem 6.8:  Write a boolean function named is_prime which takes an integer
#               as an argument, and returns True if the number is prime, and False
#               otherwise.
#               The program should prompt the user to enter an integer value before
#               calling the function, and displays whether the inputted integer is
#               True or False.
#
#
# Author: Giorgio Murad Murad

# Function
def is_prime(integer):
    for i in range(2, integer):
        if integer % i == 0:
            return False

    return True


# Prompting the user to enter an integer value
nb = int(input("Enter an integer value: "))

# Displaying Result
if is_prime(nb):
    print("The number is prime")
else:
    print("The number is not prime")