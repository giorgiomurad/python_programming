# Problem from Starting Out With Python by Tony Gaddis
# Chapter 6: Value Returning Functions & Modules
#
# Problem 6.1:  One foot is twelve inches. Write a function that accepts a number of feet as
#               an argument, and returns the number of inches.
#               The program should ask the user to enter the number of feet, before calling the
#               function, and displays the inches.
#
#
# Author: Giorgio Murad Murad

# Function that takes the number of feet, converts it to inches, and returns the value
def ftToInches(ft):
    inches = ft * 12
    return inches


# Asking the user to enter the number of feet
feet = int(input("Enter the number of feet: "))

# Calling the function, and assigning the returned value to another function
inches = ftToInches(feet)

# Displaying the number of inches
print("The number of inches is", inches)