# Problem from Starting Out With Python by Tony Gaddis
# Chapter 8: Working with Sequences: Strings and Lists
#
# Problem 8.1:  Write a program that prompts the user to enter the first, middle, and
#               last names, and displays each name's initial.
#
#               For Example:    If the user enters John William Smith, the program should display
#                               J. W. S. in the output.
#
#
# Author: Giorgio Murad Murad

# Creating a new list called user
user = []

# Prompting the user to enter the first name, and adding it to the list
first_name = input("Enter your first name: ")
user.append(first_name)

# Prompting the user to enter the middle name, and adding it to the list
middle_name = input("Enter your middle name: ")
user.append(middle_name)

# Prompting the user to enter the last name, and adding it to the list
last_name = input("Enter your last name: ")
user.append(last_name)

# Adding every element's initial to another list
initials = []
for name in user:
    initials.append(name[0])

# Joining all initials to form a single string, and saving this string
code_name = ". ".join(initials)
print("The code name is " + code_name + ". ")