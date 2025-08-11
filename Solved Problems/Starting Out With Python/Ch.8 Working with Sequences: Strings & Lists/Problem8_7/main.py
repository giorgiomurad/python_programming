# Problem from Starting Out With Python by Tony Gaddis
# Chapter 8: Working with Sequences: Strings and Lists
#
# Problem 8.7:  Write a program that reads from an external text file and displays the following:
#                   - The number of uppercase letters in the file
#                   - The number of lowercase letters in the file
#                   - The number of digits in the file
#                   - The number of white space characters in the file
#
#
# Author: Giorgio Murad Murad

# Opening the external file for reading
file = open('text.txt', 'r')

# Initializing integer variables required for this program
uppercase = 0
lowercase = 0
digits = 0
spaces = 0

# Going through the file line by line
for line in file:
    # Going through the line character by character
    for char in line:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1

# Displaying the final results
print(
    'Number of uppercase characters: {}\n'.format(uppercase),
    'Number of lowercase characters: {}\n'.format(lowercase),
    'Number of digits: {}\n'.format(digits),
    'Number of spaces: {}\n'.format(spaces),
)

# Closing the file
file.close()