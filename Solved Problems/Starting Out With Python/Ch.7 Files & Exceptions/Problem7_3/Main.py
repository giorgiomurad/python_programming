# Problem from Starting Out With Python by Tony Gaddis
# Chapter 7: Files & Exception
#
# Problem 7.3:  Write a program that asks the user for the name of the file.
#               The program should display the contents of the file with each line preceded
#               by the line number and a colon. The line numbering should start at 1.
#
#
# Author: Giorgio Murad Murad

# Asking the user to enter the name of the file
file = input('Enter the name of the file (with its extension eg: .txt):\n')

# Opening the external file for reading
f1 = open(file, 'r')

# Displaying each line from the file preceded by its line number
lineNb = 1
for line in f1:
    print('{}:\t{}'.format(lineNb, line))
    lineNb += 1

# Closing the file
f1.close()